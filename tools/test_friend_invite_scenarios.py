#!/usr/bin/env python3
"""Behavioral simulation of FMPlayerFriendsManager invite lifecycle."""

from __future__ import annotations

import copy
import sys
from dataclasses import dataclass, field
from typing import Any

INVRESP_ACCEPTED = 5
INVRESP_DECLINED = 1
INVRESP_ALREADYFRIEND = 4
MAX_FRIENDS = 300


def friend_list_contains(friends: list[int] | None, account_id: int) -> bool:
    return account_id in (friends or [])


@dataclass
class Invite:
    inviter_id: int
    inviter_data: dict[str, Any]
    invitee_id: int
    invitee_data: dict[str, Any]


@dataclass
class FriendManagerSim:
    fairies: dict[int, dict[str, Any]]
    invites_by_inviter: dict[int, Invite] = field(default_factory=dict)
    invites_by_invitee: dict[int, Invite] = field(default_factory=dict)
    online_accounts: dict[int, bool] = field(default_factory=dict)
    outbound: list[tuple[int, str, tuple]] = field(default_factory=list)
    set_fairy_failures: set[str] = field(default_factory=set)

    def online_yes_no_for(self, account_id: int) -> int:
        return 1 if self.online_accounts.get(account_id) else 0

    def fairy(self, account_id: int) -> dict[str, Any]:
        data = self.fairies[account_id]
        return {
            "_id": data["_id"],
            "name": data["name"],
            "ownerAccount": data["ownerAccount"],
            "friends": list(data.get("friends") or []),
        }

    def send(self, account_id: int, message: str, args: tuple) -> None:
        self.outbound.append((account_id, message, args))

    def clear_invite(self, invite: Invite | None) -> None:
        if invite is None:
            return
        self.invites_by_inviter.pop(invite.inviter_id, None)
        self.invites_by_invitee.pop(invite.invitee_id, None)

    def clear_invite_for_accounts(self, inviter_id: int, invitee_id: int) -> None:
        invite = self.invites_by_inviter.get(inviter_id)
        if invite is not None and invite.invitee_id == invitee_id:
            self.clear_invite(invite)
            return
        invite = self.invites_by_invitee.get(invitee_id)
        if invite is not None and invite.inviter_id == inviter_id:
            self.clear_invite(invite)
            return
        self.invites_by_inviter.pop(inviter_id, None)
        self.invites_by_invitee.pop(invitee_id, None)

    def set_fairy_data(self, play_token: str, fields: dict[str, Any]) -> bool:
        if play_token in self.set_fairy_failures:
            return False
        for fairy in self.fairies.values():
            if fairy["ownerAccount"] == play_token:
                fairy.update(copy.deepcopy(fields))
                return True
        return False

    def make_friends(self, invite: Invite) -> None:
        inviter = invite.inviter_data
        invitee = invite.invitee_data
        inviter["friends"] = list(inviter.get("friends") or [])
        invitee["friends"] = list(invitee.get("friends") or [])

        inviter_already = friend_list_contains(inviter["friends"], invite.invitee_id)
        invitee_already = friend_list_contains(invitee["friends"], invite.inviter_id)
        if inviter_already and invitee_already:
            self.clear_invite(invite)
            self.send(
                invite.inviter_id,
                "invitationResponse",
                (invite.invitee_id, INVRESP_ALREADYFRIEND, 0),
            )
            return

        inviter_needs_add = not inviter_already
        invitee_needs_add = not invitee_already

        if inviter_needs_add and len(inviter["friends"]) >= MAX_FRIENDS:
            self.clear_invite(invite)
            self.send(
                invite.inviter_id,
                "invitationResponse",
                (invite.invitee_id, INVRESP_DECLINED, 0),
            )
            return

        if invitee_needs_add and len(invitee["friends"]) >= MAX_FRIENDS:
            self.clear_invite(invite)
            self.send(
                invite.inviter_id,
                "invitationResponse",
                (invite.invitee_id, INVRESP_DECLINED, 0),
            )
            return

        inviter_added = False
        if inviter_needs_add:
            inviter["friends"].append(invite.invitee_id)
            if not self.set_fairy_data(inviter["ownerAccount"], {"friends": inviter["friends"]}):
                inviter["friends"].pop()
                self.clear_invite(invite)
                self.send(
                    invite.inviter_id,
                    "invitationResponse",
                    (invite.invitee_id, INVRESP_DECLINED, 0),
                )
                return
            inviter_added = True
            self.send(
                invite.inviter_id,
                "updatePlayerFriend",
                (invite.invitee_id, self.online_yes_no_for(invite.invitee_id)),
            )

        if invitee_needs_add:
            invitee["friends"].append(invite.inviter_id)
            if not self.set_fairy_data(invitee["ownerAccount"], {"friends": invitee["friends"]}):
                invitee["friends"].pop()
                if inviter_added:
                    inviter["friends"] = [
                        fid for fid in inviter["friends"] if fid != invite.invitee_id
                    ]
                    self.set_fairy_data(inviter["ownerAccount"], {"friends": inviter["friends"]})
                self.clear_invite(invite)
                self.send(
                    invite.inviter_id,
                    "invitationResponse",
                    (invite.invitee_id, INVRESP_DECLINED, 0),
                )
                return
            self.send(
                invite.invitee_id,
                "updatePlayerFriend",
                (invite.inviter_id, self.online_yes_no_for(invite.inviter_id)),
            )

        self.clear_invite(invite)
        self.send(
            invite.inviter_id,
            "invitationResponse",
            (invite.invitee_id, INVRESP_ACCEPTED, 0),
        )

    def request_invite(self, sender_id: int, other_player_id: int) -> None:
        if sender_id == other_player_id:
            return

        pending_accept = self.invites_by_invitee.get(sender_id)
        if pending_accept is not None:
            self.make_friends(pending_accept)
            return

        inviter_data = self.fairy(sender_id)
        invitee_data = self.fairy(other_player_id)

        if friend_list_contains(inviter_data["friends"], other_player_id) and friend_list_contains(
            invitee_data["friends"], sender_id
        ):
            self.send(sender_id, "invitationResponse", (other_player_id, INVRESP_ALREADYFRIEND, 0))
            return

        pending = self.invites_by_inviter.get(sender_id)
        if pending is not None:
            if pending.invitee_id == other_player_id:
                self.send(other_player_id, "invitationFrom", (sender_id, inviter_data["name"]))
                return
            self.clear_invite(pending)

        invite = Invite(sender_id, inviter_data, other_player_id, invitee_data)
        self.invites_by_inviter[sender_id] = invite
        self.invites_by_invitee[other_player_id] = invite
        self.send(other_player_id, "invitationFrom", (sender_id, inviter_data["name"]))

    def request_decline(self, sender_id: int, other_player_id: int, reason: int | None = None) -> None:
        if reason is None:
            self.process_invite_decline(sender_id, other_player_id, INVRESP_DECLINED)
        else:
            self.process_invite_decline(sender_id, other_player_id, reason)

    def process_invite_decline(self, decliner_id: int, inviter_id: int, response_context: int) -> None:
        self.clear_invite_for_accounts(inviter_id, decliner_id)
        self.clear_invite_for_accounts(decliner_id, inviter_id)
        if not response_context:
            response_context = INVRESP_DECLINED
        self.send(inviter_id, "invitationResponse", (decliner_id, INVRESP_DECLINED, response_context))

    def friends_of(self, account_id: int) -> list[int]:
        return list(self.fairies[account_id].get("friends") or [])

    def invite_maps_empty(self) -> bool:
        return not self.invites_by_inviter and not self.invites_by_invitee

    def last_to(self, account_id: int, message: str) -> tuple | None:
        for target, msg, args in reversed(self.outbound):
            if target == account_id and msg == message:
                return args
        return None

    def count_to(self, account_id: int, message: str) -> int:
        return sum(1 for target, msg, _ in self.outbound if target == account_id and msg == message)


def make_sim(account_ids: list[int]) -> FriendManagerSim:
    fairies = {}
    for account_id in account_ids:
        fairies[account_id] = {
            "_id": account_id * 1000,
            "name": f"Fairy{account_id}",
            "ownerAccount": f"owner{account_id}",
            "friends": [],
        }
    return FriendManagerSim(fairies=fairies)


def assert_mutual(sim: FriendManagerSim, a: int, b: int) -> None:
    if b not in sim.friends_of(a):
        raise AssertionError(f"{a} missing {b} in friends")
    if a not in sim.friends_of(b):
        raise AssertionError(f"{b} missing {a} in friends")


def assert_not_friends(sim: FriendManagerSim, a: int, b: int) -> None:
    if b in sim.friends_of(a) or a in sim.friends_of(b):
        raise AssertionError(f"{a} and {b} should not be friends")


def scenario_accept_then_third_invite() -> None:
    sim = make_sim([101, 102, 103])
    sim.request_invite(101, 102)
    sim.request_invite(102, 101)  # accept
    assert_mutual(sim, 101, 102)
    assert sim.invite_maps_empty()

    sim.outbound.clear()
    sim.request_invite(102, 103)
    if sim.last_to(103, "invitationFrom") is None:
        raise AssertionError("B->C invite must reach C (stale A->B hijack)")
    if sim.last_to(101, "invitationResponse"):
        raise AssertionError("A should not receive invitationResponse on B->C invite")


def scenario_spam_duplicate_invite() -> None:
    sim = make_sim([201, 202])
    sim.request_invite(201, 202)
    first_count = sim.count_to(202, "invitationFrom")
    sim.request_invite(201, 202)
    second_count = sim.count_to(202, "invitationFrom")
    if second_count != first_count + 1:
        raise AssertionError("duplicate invite should resend invitationFrom once more")
    if len(sim.invites_by_inviter) != 1 or sim.invites_by_inviter[201].invitee_id != 202:
        raise AssertionError("spam invite must keep single pending map for same pair")


def scenario_decline_then_reinvite() -> None:
    sim = make_sim([301, 302])
    sim.request_invite(301, 302)
    sim.request_decline(302, 301)
    if not sim.invite_maps_empty():
        raise AssertionError("decline must clear invite maps")
    resp = sim.last_to(301, "invitationResponse")
    if resp is None or resp[1] != INVRESP_DECLINED:
        raise AssertionError("decline must notify inviter")
    if resp[2] != INVRESP_DECLINED:
        raise AssertionError("decline context must be INVRESP_DECLINED for client UI event")

    sim.outbound.clear()
    sim.request_invite(301, 302)
    if sim.last_to(302, "invitationFrom") is None:
        raise AssertionError("re-invite after decline must deliver invitationFrom")


def scenario_already_friends_blocked() -> None:
    sim = make_sim([401, 402])
    sim.fairies[401]["friends"] = [402]
    sim.fairies[402]["friends"] = [401]
    sim.request_invite(401, 402)
    resp = sim.last_to(401, "invitationResponse")
    if resp is None or resp[1] != INVRESP_ALREADYFRIEND:
        raise AssertionError("already-friends must return ALREADYFRIEND to sender")
    if sim.count_to(402, "invitationFrom"):
        raise AssertionError("already-friends must not send invitationFrom")


def scenario_self_invite_ignored() -> None:
    sim = make_sim([501])
    sim.request_invite(501, 501)
    if sim.outbound:
        raise AssertionError("self-invite must be ignored")


def scenario_replace_pending_invite() -> None:
    sim = make_sim([601, 602, 603])
    sim.request_invite(601, 602)
    sim.request_invite(601, 603)
    if 602 in sim.invites_by_invitee:
        raise AssertionError("superseded pending invite to B must be cleared")
    if sim.invites_by_inviter[601].invitee_id != 603:
        raise AssertionError("pending invite should move to new target C")
    if sim.last_to(603, "invitationFrom") is None:
        raise AssertionError("new target must receive invitationFrom")


def scenario_max_friends_inviter() -> None:
    sim = make_sim([701, 702])
    sim.fairies[701]["friends"] = list(range(8000, 8000 + MAX_FRIENDS))
    sim.request_invite(701, 702)
    sim.request_invite(702, 701)
    resp = sim.last_to(701, "invitationResponse")
    if resp is None or resp[1] != INVRESP_DECLINED:
        raise AssertionError("inviter at max friends must decline")
    assert_not_friends(sim, 701, 702)


def scenario_max_friends_invitee() -> None:
    sim = make_sim([801, 802])
    sim.fairies[802]["friends"] = list(range(9000, 9000 + MAX_FRIENDS))
    sim.request_invite(801, 802)
    sim.request_invite(802, 801)
    resp = sim.last_to(801, "invitationResponse")
    if resp is None or resp[1] != INVRESP_DECLINED:
        raise AssertionError("invitee at max friends must decline")
    assert_not_friends(sim, 801, 802)


def scenario_invitee_write_fail_rollback() -> None:
    sim = make_sim([901, 902])
    sim.set_fairy_failures.add("owner902")
    sim.request_invite(901, 902)
    sim.request_invite(902, 901)
    assert_not_friends(sim, 901, 902)
    resp = sim.last_to(901, "invitationResponse")
    if resp is None or resp[1] != INVRESP_DECLINED:
        raise AssertionError("invitee write failure must decline and rollback inviter")


def scenario_inviter_write_fail() -> None:
    sim = make_sim([1001, 1002])
    sim.set_fairy_failures.add("owner1001")
    sim.request_invite(1001, 1002)
    sim.request_invite(1002, 1001)
    assert_not_friends(sim, 1001, 1002)
    resp = sim.last_to(1001, "invitationResponse")
    if resp is None or resp[1] != INVRESP_DECLINED:
        raise AssertionError("inviter write failure must decline without adding either side")


def scenario_counts_after_accept() -> None:
    sim = make_sim([1101, 1102, 1103])
    sim.request_invite(1101, 1102)
    sim.request_invite(1102, 1101)
    if len(sim.friends_of(1101)) != 1 or len(sim.friends_of(1102)) != 1:
        raise AssertionError("each side should have exactly one friend after accept")
    assert_mutual(sim, 1101, 1102)

    sim.request_invite(1102, 1103)
    sim.request_invite(1103, 1102)
    if len(sim.friends_of(1102)) != 2:
        raise AssertionError("B should have two friends after accepting C")
    assert_mutual(sim, 1102, 1103)


def scenario_decline_with_reason() -> None:
    sim = make_sim([311, 312])
    sim.request_invite(311, 312)
    sim.request_decline(312, 311, reason=64)
    resp = sim.last_to(311, "invitationResponse")
    if resp is None or resp[2] != 64:
        raise AssertionError("decline-with-reason must forward reason as invitationResponse context")


SCENARIOS = [
    ("accept then third invite (no hijack)", scenario_accept_then_third_invite),
    ("spam duplicate invite resend", scenario_spam_duplicate_invite),
    ("decline clears maps and re-invite works", scenario_decline_then_reinvite),
    ("decline with reason forwards context", scenario_decline_with_reason),
    ("already friends blocked", scenario_already_friends_blocked),
    ("self invite ignored", scenario_self_invite_ignored),
    ("replace pending invite target", scenario_replace_pending_invite),
    ("inviter at max friends declined", scenario_max_friends_inviter),
    ("invitee at max friends declined", scenario_max_friends_invitee),
    ("invitee write fail rolls back inviter", scenario_invitee_write_fail_rollback),
    ("inviter write fail aborts both sides", scenario_inviter_write_fail),
    ("friend counts after chained accepts", scenario_counts_after_accept),
]


def main() -> None:
    failed: list[tuple[str, str]] = []
    print("=== Friend invite scenario simulation ===\n")
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
    print("All invite lifecycle scenarios passed.")


if __name__ == "__main__":
    main()
