"""Panel session: settle-then-deliver with client load guard and empty sync flush."""

from __future__ import annotations

import os
import time
import urllib.error
import urllib.request
from pathlib import Path

from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import describeException
from direct.task.Task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.uberdog.leaderboard.leaderboard_registry import (
    is_seasonal_board_request,
    is_weekly_board_request,
    SUPPORTED_GAME_IDS,
)
from game.fairies.uberdog.leaderboard.leaderboard_service import (
    _board_cache_root,
    panel_guard_entry_count,
    panel_load_guard_seconds,
    preload_board_wire_cache,
    prewarm_busts_for_entries,
)

notify = DirectNotifyGlobal.directNotify.newCategory("LeaderBoardPanel")

PANEL_SESSION_IDLE_RESET_SECONDS = 120.0
PANEL_DEBOUNCE_SECONDS = 0.45

FLUSH_INTERRUPT = "interrupt_during_load"
FLUSH_SAME_BOARD = "same_board_return_during_load"

PHASE_IDLE = "idle"
PHASE_SETTLING = "settling"
PHASE_CLIENT_LOADING = "client_loading"

_PANEL_SESSIONS: dict[int, dict] = {}
_LB_TRACE_PATH = Path(__file__).resolve().parents[1] / "logs" / "lb_panel_trace.log"


def _lb_trace(message: str) -> None:
    notify.info(message)
    try:
        _LB_TRACE_PATH.parent.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with _LB_TRACE_PATH.open("a", encoding="utf-8") as handle:
            handle.write("%s %s\n" % (stamp, message))
    except OSError:
        pass


def _settle_task_name(av_id: int) -> str:
    return "lbPanelSettle-%s" % av_id


def _clear_panel_tasks(av_id: int) -> None:
    taskMgr.remove(_settle_task_name(av_id))


def clear_panel_session(av_id: int) -> None:
    """Drop all panel session state for an avatar (e.g. after panel close)."""
    _PANEL_SESSIONS.pop(av_id, None)
    _clear_panel_tasks(av_id)


def _trigger_bust_warm() -> None:
    token = os.environ.get("API_TOKEN", "")
    if not token:
        return
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:8013/fairies/api/internal/warmLeaderboardBustCache",
            data=b"",
            headers={"Authorization": token},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=3)
    except (urllib.error.URLError, OSError, ValueError):
        pass


def _wire_state_key(board_type: int) -> str:
    if is_seasonal_board_request(board_type):
        return "seasonWireByGame"
    return "weeklyWireByGame"


def _period_state_key(board_type: int) -> str:
    if is_seasonal_board_request(board_type):
        return "seasonId"
    return "weekId"


def _ensure_session_wire_cache(
    mgr, cache: dict, state: dict, board_type: int
) -> bool:
    try:
        preload_board_wire_cache(mgr.air, cache, board_type)
    except Exception:
        notify.warning("leaderboard preload failed: %s" % describeException())
        return False

    board_root = _board_cache_root(cache, board_type)
    period_id = board_root.get("_periodId")
    wire_key = _wire_state_key(board_type)
    period_key = _period_state_key(board_type)
    if state.get(period_key) == period_id and state.get(wire_key):
        return True

    wire_by_game = {
        int(game_id): list(board_root.get(game_id) or [])
        for game_id in SUPPORTED_GAME_IDS
    }
    state[wire_key] = wire_by_game
    state[period_key] = period_id
    if not state.get("bustWarmTriggered"):
        state["bustWarmTriggered"] = True
        _trigger_bust_warm()
    return True


def _wire_entries_for_game(state: dict, game_id: int, board_type: int) -> list:
    wire_key = _wire_state_key(board_type)
    wire_by_game = state.get(wire_key) or state.get("wireByGame") or {}
    entries = wire_by_game.get(int(game_id))
    if entries is None:
        return []
    return list(entries)


def _guard_seconds_for_game(state: dict, game_id: int, board_type: int) -> float:
    return panel_load_guard_seconds(
        panel_guard_entry_count(state, game_id, board_type)
    )


def _extend_load_until(
    state: dict, now: float, game_id: int, board_type: int
) -> None:
    until = now + _guard_seconds_for_game(state, game_id, board_type)
    existing = float(state.get("loadUntil") or 0.0)
    state["loadUntil"] = max(existing, until)


def _view_key(game_id: int, board_type: int) -> tuple[int, int]:
    return (int(game_id), int(board_type))


def _same_board_cooldown_remaining(
    state: dict, now: float, game_id: int, board_type: int
) -> float:
    populated_key = _view_key(game_id, board_type)
    if populated_key != tuple(state.get("lastPopulated") or ()):
        return 0.0
    if populated_key != tuple(state.get("lastDelivered") or ()):
        return 0.0
    populated_at = float(state.get("lastPopulatedAt") or 0.0)
    if populated_at <= 0.0:
        return 0.0
    return (populated_at + _guard_seconds_for_game(state, game_id, board_type)) - now


def _in_load_guard(
    state: dict,
    now: float,
    game_id: int | None = None,
    board_type: int | None = None,
) -> bool:
    if now < float(state.get("loadUntil") or 0.0):
        return True
    if game_id is None:
        return False
    remaining = _same_board_cooldown_remaining(state, now, game_id, board_type)
    if remaining > 0.001:
        populated_at = float(state.get("lastPopulatedAt") or 0.0)
        _extend_load_until(state, populated_at, game_id, board_type)
        return True
    return False


def _guard_remaining_seconds(
    state: dict, now: float, game_id: int, board_type: int
) -> float:
    load_remaining = float(state.get("loadUntil") or 0.0) - now
    cooldown_remaining = _same_board_cooldown_remaining(state, now, game_id, board_type)
    return max(load_remaining, cooldown_remaining, 0.001)


def _clear_populated_guard(state: dict) -> None:
    """Drop guard/cooldown from a prior populated board (cross-game tab switch)."""
    state.pop("loadUntil", None)
    state.pop("lastPopulated", None)
    state.pop("lastPopulatedAt", None)
    state.pop("lastEntryCount", None)


def _flush_empty(
    mgr,
    av_id: int,
    game_id: int,
    board_type: int,
    req_seq: int,
    reason: str,
    state: dict,
) -> None:
    _lb_trace(
        "lbFlush avId=%s reqSeq=%s gameId=%s boardType=%s reason=%s"
        % (av_id, req_seq, game_id, board_type, reason)
    )
    mgr.sendUpdateToAvatarId(av_id, "lbResponse", [game_id, board_type, []])
    state["lastDelivered"] = _view_key(game_id, board_type)
    now = time.monotonic()
    if reason == FLUSH_SAME_BOARD:
        _extend_load_until(state, now, game_id, board_type)
        _lb_trace(
            "lbDrain avId=%s reqSeq=%s until=%.2fs entries=%s"
            % (
                av_id,
                req_seq,
                float(state.get("loadUntil") or 0.0) - now,
                panel_guard_entry_count(state, game_id, board_type),
            )
        )
    else:
        _clear_populated_guard(state)
        _lb_trace(
            "lbFlushClear avId=%s reqSeq=%s gameId=%s reason=%s"
            % (av_id, req_seq, game_id, reason)
        )
    state["phase"] = PHASE_SETTLING


def _deliver_full(
    mgr,
    av_id: int,
    game_id: int,
    board_type: int,
    state: dict,
    req_seq: int,
) -> None:
    entries = _wire_entries_for_game(state, game_id, board_type)
    prewarm_busts_for_entries(entries)
    _lb_trace(
        "lbResponse avId=%s reqSeq=%s gameId=%s boardType=%s entries=%s phase=%s"
        % (
            av_id,
            req_seq,
            game_id,
            board_type,
            len(entries),
            state.get("phase"),
        )
    )
    mgr.sendUpdateToAvatarId(av_id, "lbResponse", [game_id, board_type, entries])
    now = time.monotonic()
    entry_count = len(entries)
    board_key = _view_key(game_id, board_type)
    state["lastEntryCount"] = entry_count
    state["lastPopulated"] = board_key
    state["lastDelivered"] = board_key
    state["lastPopulatedAt"] = now
    _extend_load_until(state, now, game_id, board_type)
    state["phase"] = PHASE_CLIENT_LOADING
    state.pop("pendingFull", None)
    _lb_trace(
        "lbGuard start avId=%s reqSeq=%s duration=%.2fs entries=%s"
        % (av_id, req_seq, float(state.get("loadUntil") or 0.0) - now, entry_count)
    )


def _cancel_pending_delivery(av_id: int, state: dict, reason: str) -> None:
    """Drop scheduled delivery (e.g. user switched weekly/seasonal tab)."""
    state["settleToken"] = int(state.get("settleToken", 0)) + 1
    state.pop("pendingFull", None)
    state.pop("settleUntil", None)
    _clear_populated_guard(state)
    state["phase"] = PHASE_IDLE
    _clear_panel_tasks(av_id)
    notify.info(
        "lbPending cancelled avId=%s reason=%s phase=%s"
        % (av_id, reason, PHASE_IDLE)
    )


def _touch_panel_view(state: dict, game_id: int, board_type: int) -> None:
    state["viewGameId"] = int(game_id)
    state["viewBoardType"] = int(board_type)
    state["lastActivity"] = time.monotonic()


def _schedule_settle_retry(mgr, av_id: int, delay: float, token: int) -> None:
    task_name = _settle_task_name(av_id)
    taskMgr.remove(task_name)
    taskMgr.doMethodLater(
        max(0.001, delay),
        _run_settle,
        task_name,
        extraArgs=[mgr, av_id, token],
        appendTask=False,
    )


def _schedule_settle(mgr, av_id: int, state: dict) -> None:
    state["settleToken"] = int(state.get("settleToken", 0)) + 1
    token = state["settleToken"]
    now = time.monotonic()
    settle_until = float(state.get("settleUntil") or now)
    ready_at = settle_until
    if _in_load_guard(
        state,
        now,
        state.get("viewGameId"),
        state.get("viewBoardType"),
    ):
        ready_at = max(settle_until, float(state.get("loadUntil") or 0.0))
    delay = max(0.001, ready_at - now)
    _schedule_settle_retry(mgr, av_id, delay, token)


def _run_settle(mgr, av_id: int, token: int) -> int:
    state = _PANEL_SESSIONS.get(av_id)
    if not state or state.get("settleToken") != token:
        notify.info(
            "lbSettle stale avId=%s token=%s current=%s"
            % (av_id, token, state.get("settleToken") if state else None)
        )
        return Task.done

    now = time.monotonic()
    settle_until = float(state.get("settleUntil") or 0.0)
    load_until = float(state.get("loadUntil") or 0.0)

    if now < settle_until:
        _schedule_settle_retry(mgr, av_id, settle_until - now, token)
        return Task.done

    pending = state.get("pendingFull")
    if not pending:
        notify.info("lbDeliver skipped avId=%s reason=no_pending" % av_id)
        if state.get("phase") == PHASE_CLIENT_LOADING and now >= load_until:
            state["phase"] = PHASE_IDLE
        return Task.done

    game_id, board_type, req_seq = pending
    game_id = int(game_id)
    board_type = int(board_type)
    req_seq = int(req_seq)

    view_game = int(state.get("viewGameId") or game_id)
    view_board = int(state.get("viewBoardType") or board_type)
    if view_game != game_id or view_board != board_type:
        notify.info(
            "lbDeliver skipped avId=%s reqSeq=%s reason=view_changed "
            "want=%s/%s view=%s/%s"
            % (av_id, req_seq, game_id, board_type, view_game, view_board)
        )
        state.pop("pendingFull", None)
        return Task.done

    if _in_load_guard(state, now, view_game, view_board):
        remaining = _guard_remaining_seconds(state, now, view_game, view_board)
        notify.info(
            "lbGuard defer avId=%s reqSeq=%s remaining=%.2fs"
            % (av_id, state.get("reqSeq"), remaining)
        )
        _schedule_settle_retry(mgr, av_id, remaining, token)
        return Task.done

    if not (
        is_weekly_board_request(view_board)
        or is_seasonal_board_request(view_board)
    ):
        notify.info(
            "lbDeliver skipped avId=%s reqSeq=%s reason=unsupported_board"
            % (av_id, req_seq)
        )
        state.pop("pendingFull", None)
        return Task.done

    notify.info(
        "lbSettle fire avId=%s reqSeq=%s gameId=%s boardType=%s"
        % (av_id, req_seq, game_id, board_type)
    )
    try:
        _deliver_full(mgr, av_id, game_id, board_type, state, req_seq)
    except Exception:
        notify.warning(
            "lbResponse failed avId=%s reqSeq=%s gameId=%s type=%s: %s"
            % (av_id, req_seq, game_id, board_type, describeException())
        )
        mgr.sendUpdateToAvatarId(av_id, "lbResponse", [game_id, board_type, []])
        state.pop("pendingFull", None)
    return Task.done


def _flush_reason_during_guard(state: dict, view_key: tuple[int, int]) -> str:
    if state.get("lastPopulated") == view_key:
        return FLUSH_SAME_BOARD
    return FLUSH_INTERRUPT


def handle_panel_lb_request(
    mgr,
    av_id: int,
    game_id: int,
    board_type: int,
    cache: dict,
) -> None:
    """Settle-then-deliver weekly/seasonal boards; empty sync flush during load guard."""
    game_id = int(game_id)
    board_type = int(board_type)

    if not (
        is_weekly_board_request(board_type)
        or is_seasonal_board_request(board_type)
    ):
        mgr.sendUpdateToAvatarId(av_id, "lbResponse", [game_id, board_type, []])
        return

    state = _PANEL_SESSIONS.setdefault(av_id, {})
    now = time.monotonic()
    last_activity = float(state.get("lastActivity") or 0.0)
    if now - last_activity > PANEL_SESSION_IDLE_RESET_SECONDS:
        notify.info("lbSession reset avId=%s idle=%.1fs" % (av_id, now - last_activity))
        state.clear()
        _clear_panel_tasks(av_id)
        now = time.monotonic()

    prev_board = state.get("viewBoardType")
    _touch_panel_view(state, game_id, board_type)
    if prev_board is not None and int(prev_board) != board_type:
        _cancel_pending_delivery(av_id, state, "board_type_switch")

    req_seq = int(state.get("reqSeq", 0)) + 1
    state["reqSeq"] = req_seq

    if not _ensure_session_wire_cache(mgr, cache, state, board_type):
        notify.warning(
            "lbRequest preload miss avId=%s reqSeq=%s gameId=%s"
            % (av_id, req_seq, game_id)
        )
        mgr.sendUpdateToAvatarId(av_id, "lbResponse", [game_id, board_type, []])
        return

    view_key = _view_key(game_id, board_type)
    in_guard = _in_load_guard(state, now, game_id, board_type)
    _lb_trace(
        "lbRequest avId=%s reqSeq=%s gameId=%s boardType=%s phase=%s lastPopulated=%s inGuard=%s"
        % (
            av_id,
            req_seq,
            game_id,
            board_type,
            state.get("phase", PHASE_IDLE),
            state.get("lastPopulated"),
            in_guard,
        )
    )

    if in_guard:
        reason = _flush_reason_during_guard(state, view_key)
        _flush_empty(mgr, av_id, game_id, board_type, req_seq, reason, state)
        in_guard = (
            False
            if reason == FLUSH_INTERRUPT
            else _in_load_guard(state, now, game_id, board_type)
        )

    state["pendingFull"] = (game_id, board_type, req_seq)
    state["settleUntil"] = now + PANEL_DEBOUNCE_SECONDS
    if not in_guard:
        state["phase"] = PHASE_SETTLING
        _lb_trace(
            "lbPhase avId=%s reqSeq=%s -> %s"
            % (av_id, req_seq, PHASE_SETTLING)
        )

    _schedule_settle(mgr, av_id, state)
