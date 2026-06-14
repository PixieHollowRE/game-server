from __future__ import annotations

MORE_OPTIONS_ALPHABET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
)
MORE_OPTIONS_EMPTY = "A" * 24
FAVORITE_BADGE_OFFSET = 10


def decode_more_options(more_options: str) -> bytes:
    if not more_options or len(more_options) != 24:
        return b""

    bits = 0
    bit_count = 0
    decoded = bytearray()

    for char in more_options:
        try:
            value = MORE_OPTIONS_ALPHABET.index(char)
        except ValueError:
            return b""

        bits = (bits << 6) | value
        bit_count += 6
        while bit_count >= 8:
            bit_count -= 8
            decoded.append((bits >> bit_count) & 0xFF)

    return bytes(decoded)


def encode_more_options(raw: bytes) -> str:
    if len(raw) < 18:
        raw = raw.ljust(18, b"\x00")

    bits = 0
    bit_count = 0
    encoded: list[str] = []

    for byte in raw[:18]:
        bits = (bits << 8) | byte
        bit_count += 8
        while bit_count >= 6:
            bit_count -= 6
            index = (bits >> bit_count) & 0x3F
            encoded.append(MORE_OPTIONS_ALPHABET[index])

    if bit_count:
        bits <<= 6 - bit_count
        encoded.append(MORE_OPTIONS_ALPHABET[bits & 0x3F])

    return "".join(encoded)[:24].ljust(24, "A")


def normalize_more_options(more_options: str) -> str:
    if not more_options or len(more_options) != 24:
        return MORE_OPTIONS_EMPTY

    if set(more_options) == {"0"}:
        return MORE_OPTIONS_EMPTY

    if any(char not in MORE_OPTIONS_ALPHABET for char in more_options):
        return MORE_OPTIONS_EMPTY

    return more_options


def parse_favorite_badge_from_more_options(more_options: str) -> int:
    decoded = decode_more_options(normalize_more_options(more_options))
    if len(decoded) < FAVORITE_BADGE_OFFSET + 2:
        return 0

    badge_id = decoded[FAVORITE_BADGE_OFFSET] | (
        decoded[FAVORITE_BADGE_OFFSET + 1] << 8
    )
    if badge_id < 10000 or badge_id > 32767:
        return 0

    return badge_id


def find_favorite_badge_in_more_options(
    more_options: str, earned_badge_ids: set[int] | None = None
) -> int:
    earned_badge_ids = earned_badge_ids or set()
    parsed = parse_favorite_badge_from_more_options(more_options)
    if parsed in earned_badge_ids:
        return parsed

    decoded = decode_more_options(normalize_more_options(more_options))
    if len(decoded) < 18:
        return 0

    matches: list[tuple[int, int]] = []
    for offset in range(0, 17):
        badge_id = decoded[offset] | (decoded[offset + 1] << 8)
        if (
            badge_id >= 10000
            and badge_id <= 32767
            and badge_id in earned_badge_ids
        ):
            matches.append((offset, badge_id))

    if not matches:
        return 0

    for preferred_offset in (FAVORITE_BADGE_OFFSET, 16):
        for offset, badge_id in matches:
            if offset == preferred_offset:
                return badge_id

    return matches[0][1]


def _pick_favorite_id(
    parsed: int,
    favorite_badge_id: int,
    earned_badge_ids: set[int],
) -> int:
    if parsed in earned_badge_ids:
        return parsed
    if favorite_badge_id in earned_badge_ids:
        return favorite_badge_id
    return 0


def is_corrupt_more_options(
    more_options: str, earned_badge_ids: set[int] | None = None
) -> bool:
    earned_badge_ids = earned_badge_ids or set()
    more_options = normalize_more_options(more_options)
    if more_options == MORE_OPTIONS_EMPTY:
        return False

    decoded = decode_more_options(more_options)
    if len(decoded) != 18:
        return True

    favorite = parse_favorite_badge_from_more_options(more_options)
    if (
        favorite >= 10000
        and earned_badge_ids
        and favorite not in earned_badge_ids
    ):
        return True

    return False


def set_favorite_in_more_options(more_options: str, favorite: int) -> str:
    more_options = normalize_more_options(more_options)
    decoded = bytearray(decode_more_options(more_options))
    if len(decoded) < 18:
        decoded.extend(b"\x00" * (18 - len(decoded)))

    decoded[FAVORITE_BADGE_OFFSET] = favorite & 0xFF
    decoded[FAVORITE_BADGE_OFFSET + 1] = (favorite >> 8) & 0xFF
    return encode_more_options(bytes(decoded[:18]))


def resolve_favorite_badge(
    more_options: str,
    favorite_badge_id: int = 0,
    earned_badge_ids: set[int] | None = None,
) -> tuple[str, int]:
    """Return repaired moreOptions and favoriteBadgeId; preserve stored favorite when earned."""
    earned_badge_ids = earned_badge_ids or set()
    more_options = normalize_more_options(more_options)
    stored = int(favorite_badge_id or 0)
    parsed = parse_favorite_badge_from_more_options(more_options)
    favorite = _pick_favorite_id(parsed, stored, earned_badge_ids)

    if is_corrupt_more_options(more_options, earned_badge_ids):
        base = MORE_OPTIONS_EMPTY
        if favorite > 0:
            repaired = set_favorite_in_more_options(base, favorite)
            return repaired, favorite
        if parsed > 0 and parsed not in earned_badge_ids:
            return set_favorite_in_more_options(base, 0), 0
        return base, 0

    if favorite > 0:
        repaired = set_favorite_in_more_options(more_options, favorite)
        return repaired, favorite

    if parsed > 0 and parsed not in earned_badge_ids:
        return set_favorite_in_more_options(more_options, 0), 0

    return more_options, 0


def repair_more_options(
    more_options: str,
    favorite_badge_id: int = 0,
    earned_badge_ids: set[int] | None = None,
) -> str:
    repaired, _favorite = resolve_favorite_badge(
        more_options,
        favorite_badge_id,
        earned_badge_ids,
    )
    return repaired


def persist_more_options(air, av_id: int, more_options: str) -> None:
    fairy = air.mongoInterface.mongodb.fairies.find_one({"_id": av_id}) or {}
    earned_badge_ids = {
        int(entry["badgeId"]) for entry in (fairy.get("earnedBadges") or [])
    }
    stored = int(fairy.get("favoriteBadgeId") or 0)
    more_options, favorite_badge_id = resolve_favorite_badge(
        more_options,
        stored,
        earned_badge_ids,
    )

    air.mongoInterface.updateFields(
        "fairies",
        {
            "moreOptions": more_options,
            "favoriteBadgeId": favorite_badge_id,
        },
        av_id,
    )
