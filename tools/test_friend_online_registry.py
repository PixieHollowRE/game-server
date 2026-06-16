#!/usr/bin/env python3
"""Unit tests for FM account-session online registry (not DBSS activation)."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import Any


def online_yes_no_for_account(online_accounts: dict[int, bool], account_id: int) -> int:
    return 1 if online_accounts.get(account_id) is True else 0


@dataclass
class OnlineRegistrySim:
    fairies: dict[int, dict[str, Any]]
    online_accounts: dict[int, bool] = field(default_factory=dict)
    outbound: list[tuple[int, str, tuple]] = field(default_factory=list)

    def handle_online(self, account_id: int) -> None:
        self.online_accounts[account_id] = True
        account = self.fairies[account_id]
        for friend_id in account.get("friends") or []:
            self.outbound.append(
                (friend_id, "updatePlayerFriend", (account_id, 1))
            )
        for friend_id in account.get("friends") or []:
            online = online_yes_no_for_account(self.online_accounts, friend_id)
            self.outbound.append(
                (account_id, "updatePlayerFriend", (friend_id, online))
            )

    def handle_offline(self, account_id: int) -> None:
        self.online_accounts.pop(account_id, None)
        account = self.fairies[account_id]
        for friend_id in account.get("friends") or []:
            self.outbound.append(
                (friend_id, "updatePlayerFriend", (account_id, 0))
            )

    def make_friends_online(
        self, inviter_id: int, invitee_id: int, inviter_online: bool, invitee_online: bool
    ) -> None:
        if inviter_online:
            self.online_accounts[inviter_id] = True
        if invitee_online:
            self.online_accounts[invitee_id] = True
        inviter = self.fairies[inviter_id]
        invitee = self.fairies[invitee_id]
        inviter.setdefault("friends", []).append(invitee_id)
        invitee.setdefault("friends", []).append(inviter_id)
        self.outbound.append(
            (
                inviter_id,
                "updatePlayerFriend",
                (invitee_id, online_yes_no_for_account(self.online_accounts, invitee_id)),
            )
        )
        self.outbound.append(
            (
                invitee_id,
                "updatePlayerFriend",
                (inviter_id, online_yes_no_for_account(self.online_accounts, inviter_id)),
            )
        )

    def last_friend_online_to(self, account_id: int, friend_account_id: int) -> int | None:
        for target, msg, args in reversed(self.outbound):
            if target == account_id and msg == "updatePlayerFriend" and args[0] == friend_account_id:
                return args[1]
        return None


def make_sim() -> OnlineRegistrySim:
    return OnlineRegistrySim(
        fairies={
            101: {"_id": 101000, "name": "A", "friends": [102]},
            102: {"_id": 102000, "name": "B", "friends": [101]},
        }
    )


def test_friend_in_activity_shows_online_on_login() -> None:
    """Friend logged in (in minigame) before B logs in — B must see online=1."""
    sim = make_sim()
    sim.handle_online(102)  # A already in game; session registered
    sim.outbound.clear()
    sim.handle_online(101)  # B logs in, builds friend list
    online = sim.last_friend_online_to(101, 102)
    if online != 1:
        raise AssertionError(f"expected friend online=1 during activity, got {online}")


def test_friend_offline_after_logout() -> None:
    sim = make_sim()
    sim.handle_online(101)
    sim.handle_online(102)
    sim.outbound.clear()
    sim.handle_offline(102)
    online = sim.last_friend_online_to(101, 102)
    if online != 0:
        raise AssertionError(f"expected friend offline=0 after logout, got {online}")


def test_login_sync_ignores_dbss_activation_false() -> None:
    """Registry says online even when Stateserver GET_ACTIVATED would be false."""
    sim = make_sim()
    sim.online_accounts[102] = True
    activated_from_dbss = False
    online = online_yes_no_for_account(sim.online_accounts, 102)
    if online != 1:
        raise AssertionError("registry must trump DBSS activation=false")
    if activated_from_dbss:
        raise AssertionError("test setup: DBSS should simulate false")


def test_make_friends_reflects_online_registry() -> None:
    sim = make_sim()
    sim.fairies[101]["friends"] = []
    sim.fairies[102]["friends"] = []
    sim.make_friends_online(101, 102, inviter_online=True, invitee_online=False)
    if sim.last_friend_online_to(101, 102) != 0:
        raise AssertionError("offline invitee should be 0")
    if sim.last_friend_online_to(102, 101) != 1:
        raise AssertionError("online inviter should be 1")


def test_lua_source_uses_registry_not_dbss_for_login_sync() -> None:
    from pathlib import Path

    lua = (Path(__file__).resolve().parents[1] / "config" / "FMPlayerFriendsManager.lua").read_text(
        encoding="utf-8"
    )
    if "onlineAccounts" not in lua:
        raise AssertionError("missing onlineAccounts table")
    if "onlineYesNoForAccount" not in lua:
        raise AssertionError("missing onlineYesNoForAccount helper")
    if "queryDBSS(participant, friendAccount._id" in lua:
        raise AssertionError("handleOnline still gates friend list on queryDBSS")
    if "onlineYesNoForAccount(invite.inviteeId)" not in lua:
        raise AssertionError("makeFriends must use registry for invitee online")


SCENARIOS = [
    ("friend in activity shows online on login", test_friend_in_activity_shows_online_on_login),
    ("friend offline after logout", test_friend_offline_after_logout),
    ("registry ignores DBSS activation false", test_login_sync_ignores_dbss_activation_false),
    ("make friends reflects online registry", test_make_friends_reflects_online_registry),
    ("lua source uses registry not dbss", test_lua_source_uses_registry_not_dbss_for_login_sync),
]


def main() -> None:
    failed: list[tuple[str, str]] = []
    print("=== Friend online registry tests ===\n")
    for name, fn in SCENARIOS:
        try:
            fn()
            print(f"  OK  {name}")
        except AssertionError as exc:
            failed.append((name, str(exc)))
            print(f"  FAIL  {name}: {exc}")

    print(f"\nPassed: {len(SCENARIOS) - len(failed)}/{len(SCENARIOS)}")
    if failed:
        sys.exit(1)
    print("All online registry tests passed.")


if __name__ == "__main__":
    main()
