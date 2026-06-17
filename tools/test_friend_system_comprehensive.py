#!/usr/bin/env python3
"""Comprehensive local friend system + friendship badge tests."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from panda3d.core import ConfigVariableString, loadPrcFile

GAME_SERVER = Path(__file__).resolve().parents[1]
REPO_ROOT = GAME_SERVER.parent
TOOLS = GAME_SERVER / "tools"
sys.path.insert(0, str(GAME_SERVER))
sys.path.insert(0, str(TOOLS))
LUA_PATHS = [
    GAME_SERVER / "config" / "FMPlayerFriendsManager.lua",
]

loadPrcFile(str(GAME_SERVER / "config" / "config.prc"))
if (GAME_SERVER / "config" / "local.prc").exists():
    loadPrcFile(str(GAME_SERVER / "config" / "local.prc"))


def _mongo_uri() -> str:
    host = ConfigVariableString("mongodb-host", "mongodb://127.0.0.1:27017").getValue()
    name = ConfigVariableString("mongodb-name", "PixieHollow").getValue()
    return host.rstrip("/") + "/" + name


MONGO_URI = _mongo_uri()
API_BASE = ConfigVariableString(
    "friend-test-api-base", "http://127.0.0.1:8013/fairies/api/internal"
).getValue()
API_TOKEN = ConfigVariableString("api-token", "").getValue()


class TestResult:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.failed: list[tuple[str, str]] = []
        self.warned: list[str] = []

    def ok(self, name: str) -> None:
        self.passed.append(name)

    def fail(self, name: str, detail: str) -> None:
        self.failed.append((name, detail))

    def warn(self, message: str) -> None:
        self.warned.append(message)


def run_validate_friend_badges(result: TestResult) -> None:
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "validate_friend_badges.py")],
        capture_output=True,
        text=True,
        cwd=str(GAME_SERVER),
    )
    if proc.returncode == 0:
        result.ok("validate_friend_badges.py")
    else:
        result.fail(
            "validate_friend_badges.py",
            (proc.stdout + proc.stderr).strip() or f"exit {proc.returncode}",
        )


def audit_local_mongo(result: TestResult) -> None:
    from pymongo import MongoClient

    from inspect_friend_badge_state import analyze_doc

    client = MongoClient(MONGO_URI)
    fairies = client.get_default_database()["fairies"]
    docs = list(
        fairies.find(
            {},
            {
                "_id": 1,
                "name": 1,
                "ownerAccount": 1,
                "friends": 1,
                "friendsAccepted": 1,
                "earnedBadges": 1,
                "badgeProgress": 1,
            },
        )
    )

    if not docs:
        result.warn("Mongo audit: no fairies in database")
        return

    issue_rows = []
    early_social = []

    for doc in docs:
        row = analyze_doc(doc)
        if row["issues"]:
            issue_rows.append(row)
        earned = set(row["friend_badges_earned"])
        if 10533 in earned and row["friends_unique"] < 25:
            early_social.append(row)

    result.ok(f"Mongo audit scanned {len(docs)} fairy(ies)")

    if issue_rows:
        result.warn(
            f"Mongo audit: {len(issue_rows)} fairy(ies) with friend/badge desync"
        )
        for row in issue_rows[:5]:
            result.warn(
                f"  {row['name'] or row['owner']}: {', '.join(row['issues'])}"
            )
    else:
        result.ok("Mongo audit: no desync issues")

    if early_social:
        result.fail(
            "Mongo early Social Butterfly",
            f"{len(early_social)} fairy(ies) have badge 10533 with <25 unique friends",
        )
    else:
        result.ok("Mongo: no early Social Butterfly (10533 with <25 friends)")


def check_lua_friend_guards(result: TestResult) -> None:
    required_patterns = [
        ("friendListContains", r"function friendListContains"),
        ("clearInvite helper", r"function clearInvite"),
        ("clearInvite after makeFriends", r"clearInvite\(invite\)"),
        ("clearInviteForAccounts", r"function clearInviteForAccounts"),
        ("setFairyData returns bool", r"return false"),
        ("setFairyData success log", r"setFairyData ok playToken"),
        ("duplicate guard", r"INVRESP_ALREADYFRIEND"),
        ("inviter badge credit", r"applyFriendBadge\(participant, invite\.inviterData\._id\)"),
        ("invitee badge credit", r"applyFriendBadge\(participant, invite\.inviteeData\._id\)"),
        ("abort on setFairyData fail", r"if not setFairyData"),
        ("inviter rollback on invitee fail", r"rolled back inviter"),
        ("preflight max friends", r"inviterNeedsAdd and #invite\.inviterData\.friends >= MAX_FRIENDS"),
        ("requestInvite already-friends guard", r"friendListContains\(inviterData\.friends, otherPlayerId\)"),
        ("pending duplicate resend", r"pending\.inviteeId == otherPlayerId"),
        ("offline undeclare", r"undeclareFriend\(participant, friendAccount\._id, account\._id\)"),
        ("requestDeclineWithReason handler", r"function handleFMPlayerFriendsManager_requestDeclineWithReason"),
        ("processInviteDecline helper", r"function processInviteDecline"),
        ("online session registry", r"onlineAccounts"),
        ("onlineYesNoForAccount helper", r"function onlineYesNoForAccount"),
        ("post-accept online from registry", r"onlineYesNoForAccount\(invite\.inviteeId\)"),
    ]
    forbidden_patterns = [
        ("no blind status reset", r"status = INVRESP_ACCEPTED\s*\n\s*if #invite\.inviteeData\.friends"),
    ]

    for lua_path in LUA_PATHS:
        if not lua_path.is_file():
            result.warn(f"Lua file missing: {lua_path}")
            continue

        source = lua_path.read_text(encoding="utf-8")
        label = lua_path.relative_to(REPO_ROOT)
        missing = [name for name, pattern in required_patterns if not re.search(pattern, source)]
        forbidden = [name for name, pattern in forbidden_patterns if re.search(pattern, source)]
        if missing:
            result.fail(f"Lua guards {label}", f"missing: {', '.join(missing)}")
        elif forbidden:
            result.fail(f"Lua guards {label}", f"forbidden pattern: {', '.join(forbidden)}")
        else:
            result.ok(f"Lua guards {label}")


def check_lua_stale_invite_hijack_guard(result: TestResult) -> None:
    """Regression: after accept, invite maps must clear so B->C is not hijacked by stale A->B."""
    for lua_path in LUA_PATHS:
        if not lua_path.is_file():
            continue
        source = lua_path.read_text(encoding="utf-8")
        label = lua_path.relative_to(REPO_ROOT)

        if not re.search(
            r"INVRESP_ALREADYFRIEND, 0\}\)\s*\n\s*return\s*\n\s*end",
            source,
        ):
            result.fail(f"stale-invite guard {label}", "already-friends path missing early return")
            continue

        if not re.search(
            r"clearInvite\(invite\)\s*\n\s*participant:sendUpdateToAccountId\(invite\.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,\s*\n\s*\"FMPlayerFriendsManager\", \"invitationResponse\", \{invite\.inviteeId, INVRESP_ACCEPTED",
            source,
            re.S,
        ):
            result.fail(
                f"stale-invite guard {label}",
                "makeFriends must clear invite maps before ACCEPTED invitationResponse",
            )
        else:
            result.ok(f"stale-invite guard {label}")

        if "clearInvite(pending)" not in source:
            result.fail(f"stale-invite guard {label}", "requestInvite must clear superseded pending invites")
        else:
            result.ok(f"requestInvite stale cleanup {label}")


def check_web_api_friends_dedup(result: TestResult) -> None:
    api_paths = [
        REPO_ROOT / "web-api" / "services" / "WebService.js",
        REPO_ROOT / "web-api-main" / "services" / "WebService.js",
    ]
    required = [
        ("sanitizeFriendsForWrite", r"async function sanitizeFriendsForWrite"),
        ("dedupe preserve order", r"function dedupeFriendsPreserveOrder"),
        ("setFairyData calls sanitize", r"sanitizeFriendsForWrite\(data\.fieldData\.friends, fairy\)"),
        ("reject fairy _id in friends", r"id === fairyId"),
    ]
    for api_path in api_paths:
        if not api_path.is_file():
            result.warn(f"WebService missing: {api_path}")
            continue
        source = api_path.read_text(encoding="utf-8")
        label = api_path.relative_to(REPO_ROOT)
        missing = [name for name, pattern in required if not re.search(pattern, source)]
        if missing:
            result.fail(f"API friends dedup {label}", f"missing: {', '.join(missing)}")
        else:
            result.ok(f"API friends dedup {label}")


def check_badge_progress_logic(result: TestResult) -> None:
    from game.fairies.badges.BadgeProgressService import (
        _friends_accepted_total,
        _unique_friend_ids,
        apply_friend_accepted_progress,
        ensure_friend_badges_bootstrapped,
    )

    dup_doc = {
        "_id": 1,
        "earnedBadges": [],
        "badgeProgress": [],
        "unlockedPages": [],
        "friends": [10] * 25,
        "friendsAccepted": 25,
    }
    fixed, _ = ensure_friend_badges_bootstrapped(dup_doc)
    if _friends_accepted_total(fixed) != 1:
        result.fail("unique friend count", f"expected 1 got {_friends_accepted_total(fixed)}")
    else:
        result.ok("duplicate friends count as 1 unique")

    inflated = {
        "_id": 2,
        "earnedBadges": [],
        "badgeProgress": [],
        "unlockedPages": [],
        "friends": [],
        "friendsAccepted": 25,
    }
    fixed2, _ = ensure_friend_badges_bootstrapped(inflated)
    if int(fixed2.get("friendsAccepted") or 0) != 0:
        result.fail("inflated friendsAccepted", "expected 0 after bootstrap")
    else:
        result.ok("inflated friendsAccepted ignored without friends list")

    class MiniAir:
        def __init__(self) -> None:
            self.docs = {
                99: {
                    "_id": 99,
                    "earnedBadges": [],
                    "badgeProgress": [],
                    "unlockedPages": [],
                    "friends": [],
                    "friendsAccepted": 0,
                }
            }

        @property
        def mongoInterface(self):
            return self

        @property
        def mongodb(self):
            return self

        class _Fairies:
            def __init__(self, air) -> None:
                self.air = air

            def find_one(self, query, _fields=None):
                return dict(self.air.docs.get(query["_id"], {"_id": query["_id"]}))

            def update_one(self, query, update, upsert=False):
                self.air.docs.setdefault(query["_id"], {"_id": query["_id"]}).update(
                    update.get("$set", {})
                )

        @property
        def fairies(self):
            return self._Fairies(self)

    class MiniBadgeMgr:
        def __init__(self) -> None:
            self.air = MiniAir()
            self.updates = []

        def sendUpdateToAvatarId(self, av_id, message, args):
            self.updates.append((av_id, message, args))

    mgr = MiniBadgeMgr()
    apply_friend_accepted_progress(mgr, 99)
    if mgr.air.docs[99]["friendsAccepted"] != 0:
        result.fail("accept without friends", "friendsAccepted incremented without friends[]")
    else:
        result.ok("accept without friends list does not increment")

    mgr.air.docs[99]["friends"] = [501, 502]
    apply_friend_accepted_progress(mgr, 99)
    if mgr.air.docs[99]["friendsAccepted"] != 2:
        result.fail("accept with friends", f"expected 2 got {mgr.air.docs[99]['friendsAccepted']}")
    else:
        result.ok("accept uses unique friends list length")

    if len(_unique_friend_ids({"friends": [1, 1, 2]})) != 2:
        result.fail("_unique_friend_ids", "dedupe failed")
    else:
        result.ok("_unique_friend_ids dedupes")


def test_set_fairy_data_http(result: TestResult) -> None:
    try:
        import urllib.error
        import urllib.request
    except ImportError:
        result.warn("HTTP test skipped: urllib unavailable")
        return

    if not API_TOKEN:
        result.warn("HTTP setFairyData test skipped: api-token not set in config")
        return

    from pymongo import MongoClient

    client = MongoClient(MONGO_URI)
    fairy = client.get_default_database()["fairies"].find_one(
        {"ownerAccount": {"$exists": True, "$ne": ""}},
        {"_id": 1, "ownerAccount": 1, "friends": 1},
    )
    if not fairy:
        result.warn("HTTP setFairyData test skipped: no fairy with ownerAccount")
        return

    owner = fairy["ownerAccount"]
    original_friends = list(fairy.get("friends") or [])
    probe_friend = 999999991
    test_friends = original_friends + [probe_friend]

    payload = json.dumps({
        "playToken": owner,
        "fieldData": {"friends": test_friends},
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{API_BASE}/setFairyData",
        data=payload,
        headers={
            "Authorization": API_TOKEN,
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status != 200:
                result.fail("HTTP setFairyData", f"status {resp.status}")
                return
    except urllib.error.URLError as exc:
        result.warn(f"HTTP setFairyData skipped: web-api not reachable ({exc})")
        return

    reloaded = client.get_default_database()["fairies"].find_one(
        {"_id": fairy["_id"]},
        {"friends": 1},
    )
    saved = list(reloaded.get("friends") or [])
    if probe_friend not in saved:
        result.fail("HTTP setFairyData persist", "probe friend id not saved to Mongo")
    else:
        result.ok("HTTP setFairyData writes friends[] to Mongo")

    dedupe_payload = json.dumps({
        "playToken": owner,
        "fieldData": {"friends": saved + [probe_friend, probe_friend]},
    }).encode("utf-8")
    dedupe_req = urllib.request.Request(
        f"{API_BASE}/setFairyData",
        data=dedupe_payload,
        headers={
            "Authorization": API_TOKEN,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(dedupe_req, timeout=5) as resp:
            if resp.status != 200:
                result.fail("HTTP setFairyData dedup", f"status {resp.status}")
            else:
                deduped = list(
                    client.get_default_database()["fairies"].find_one(
                        {"_id": fairy["_id"]},
                        {"friends": 1},
                    ).get("friends") or []
                )
                if deduped.count(probe_friend) != 1:
                    result.fail(
                        "HTTP setFairyData dedup",
                        f"expected one probe friend entry, got {deduped.count(probe_friend)}",
                    )
                else:
                    result.ok("HTTP setFairyData dedupes duplicate friends[] entries")
    except urllib.error.URLError as exc:
        result.warn(f"HTTP setFairyData dedup skipped: {exc}")

    # restore
    restore_payload = json.dumps({
        "playToken": owner,
        "fieldData": {"friends": original_friends},
    }).encode("utf-8")
    restore_req = urllib.request.Request(
        f"{API_BASE}/setFairyData",
        data=restore_payload,
        headers={
            "Authorization": API_TOKEN,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(restore_req, timeout=5)
        result.ok("HTTP setFairyData restore original friends")
    except urllib.error.URLError:
        result.warn("HTTP setFairyData restore failed — manual cleanup may be needed")


def test_repair_dry_run(result: TestResult) -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(TOOLS / "inspect_friend_badge_state.py"),
            "--issues-only",
        ],
        capture_output=True,
        text=True,
        cwd=str(GAME_SERVER),
    )
    if proc.returncode != 0:
        result.fail("inspect_friend_badge_state.py", proc.stderr.strip() or proc.stdout.strip())
        return

    result.ok("inspect_friend_badge_state.py --issues-only")
    if "ISSUES:" in proc.stdout:
        result.warn("inspect found issues (run with --repair to fix)")
    else:
        result.ok("inspect: no issues in database")


def run_invite_scenario_simulation(result: TestResult) -> None:
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "test_friend_invite_scenarios.py")],
        capture_output=True,
        text=True,
        cwd=str(GAME_SERVER),
    )
    if proc.returncode == 0:
        result.ok("invite lifecycle scenario simulation (12 cases)")
    else:
        result.fail(
            "invite lifecycle scenario simulation",
            (proc.stdout + proc.stderr).strip() or f"exit {proc.returncode}",
        )


def main() -> None:
    result = TestResult()

    print("=== Friend system comprehensive tests ===\n")

    run_validate_friend_badges(result)
    check_badge_progress_logic(result)
    check_lua_friend_guards(result)
    check_lua_stale_invite_hijack_guard(result)
    check_web_api_friends_dedup(result)
    run_invite_scenario_simulation(result)
    audit_local_mongo(result)
    test_repair_dry_run(result)
    test_set_fairy_data_http(result)

    print(f"\nPassed: {len(result.passed)}")
    for name in result.passed:
        print(f"  OK  {name}")

    if result.warned:
        print(f"\nWarnings: {len(result.warned)}")
        for message in result.warned:
            print(f"  WARN  {message}")

    if result.failed:
        print(f"\nFailed: {len(result.failed)}")
        for name, detail in result.failed:
            print(f"  FAIL  {name}: {detail}")
        sys.exit(1)

    print("\nAll comprehensive friend system checks passed.")
    if result.warned:
        print("Review warnings above for local data issues.")


if __name__ == "__main__":
    main()
