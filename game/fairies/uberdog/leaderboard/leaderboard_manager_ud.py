from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.showbase.PythonUtil import describeException
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.uberdog.leaderboard.leaderboard_registry import is_weekly_board_request
from game.fairies.uberdog.leaderboard.leaderboard_refresh import (
    previous_week_id,
    schedule_hourly_refresh,
    schedule_next_rollover,
    schedule_season_rollover,
)
from game.fairies.uberdog.leaderboard.leaderboard_panel import handle_panel_lb_request
from game.fairies.uberdog.leaderboard.leaderboard_honors import grant_weekly_game_champion_badges
from game.fairies.uberdog.leaderboard.leaderboard_service import (
    bind_score_cache,
    preload_seasonal_wire_cache,
    preload_weekly_wire_cache,
    rebuild_leaderboard_data,
    rebuild_seasonal_leaderboard_data,
)

notify = DirectNotifyGlobal.directNotify.newCategory("LeaderBoardMgrUD")


class LeaderBoardMgrUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)
        self._cache: dict = {}
        bind_score_cache(self._cache)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)
        try:
            rebuild_leaderboard_data(self.air)
            preload_weekly_wire_cache(self.air, self._cache)
            preload_seasonal_wire_cache(self.air, self._cache)
            schedule_next_rollover(taskMgr, self._weekly_rollover)
            schedule_season_rollover(taskMgr, self._season_rollover)
            schedule_hourly_refresh(taskMgr, self._hourly_refresh)
            notify.info("LeaderBoardMgrUD ready with leaderboard_data")
        except Exception:
            notify.warning(
                "LeaderBoardMgrUD startup failed: %s" % describeException()
            )

    def _weekly_rollover(self) -> None:
        try:
            closing_week = previous_week_id()
            grant_weekly_game_champion_badges(self.air, closing_week)
            rebuild_leaderboard_data(self.air, rollover=True)
            notify.info(
                "Weekly leaderboard rollover completed weekId=%s" % closing_week
            )
        except Exception:
            notify.warning(
                "Weekly leaderboard rollover failed: %s" % describeException()
            )

    def _season_rollover(self) -> None:
        try:
            rebuild_seasonal_leaderboard_data(self.air, rollover=True)
            preload_seasonal_wire_cache(self.air, self._cache)
            notify.info("Seasonal leaderboard rollover completed")
        except Exception:
            notify.warning(
                "Seasonal leaderboard rollover failed: %s" % describeException()
            )

    def _hourly_refresh(self) -> None:
        notify.info("Leaderboard hourly refresh starting (weekly + seasonal)...")
        try:
            rebuild_leaderboard_data(self.air)
            notify.info("Leaderboard snapshots rebuilt — warming wire caches...")
            preload_weekly_wire_cache(self.air, self._cache)
            preload_seasonal_wire_cache(self.air, self._cache)
            notify.info("Leaderboard hourly refresh complete — weekly and seasonal wire caches are hot")
        except Exception:
            notify.warning(
                "Leaderboard hourly refresh failed: %s" % describeException()
            )

    def lbRequest(self, gameId: int, boardType: int) -> None:
        av_id = self.air.getAvatarIdFromSender()
        try:
            handle_panel_lb_request(self, av_id, gameId, boardType, self._cache)
        except Exception:
            notify.warning(
                "lbRequest failed avId=%s gameId=%s type=%s: %s"
                % (av_id, gameId, boardType, describeException())
            )
            self.sendUpdateToAvatarId(av_id, "lbResponse", [gameId, boardType, []])

    def forceRollover(self, boardType: int) -> None:
        if not is_weekly_board_request(boardType):
            return
        self._weekly_rollover()
