import game.fairies.ai.FairiesConstants as fc
from .WeightedSampling import draw_without_replacement
from .DailyChanceConstants import (
    Gender,
    Category,
    DEFAULT_WEIGHT_BY_RARITY,
    DEFAULT_RARITY_BY_CATEGORY,
    SPIN_DYES,
    SPIN_COOKIES,
    SPIN_HOME_ITEMS,
    SPIN_WARDROBE_FAIRIES,
    SPIN_WARDROBE_SPARROWS,
    SPIN_BADGE_IDS,
)
from dataclasses import dataclass

# ───────────────────────────────────── POOL ITEM ──────────────────────────────────── #
@dataclass(frozen=True)
class PoolItem:
    id: int
    category: Category
    rarity: fc.Rarity # draw weight - the category default unless the item names its own
    prize_rarity: fc.Rarity | None = None  # per-item - only consulted at grant time for quantity (ING/COOKIES)
    gender: Gender | None = None
    c1: int | None = None
    c2: int | None = None

    @property
    def weight(self) -> float:
        return DEFAULT_WEIGHT_BY_RARITY[self.rarity]

    @property
    def variant_key(self) -> tuple:
        return (self.id, self.c1, self.c2)

# ──────────────────────────────────── BUILD POOL ──────────────────────────────────── #
def _build_master_pool() -> list[PoolItem]:
    pool: list[PoolItem] = []

    # Ingredients - flat draw odds (category default),
    # the per-item rarity only determines prize quantity, not the draw likelihood.
    ingredient_draw_rarity = DEFAULT_RARITY_BY_CATEGORY[Category.INGREDIENT]
    for ingredient in fc.INGREDIENTS.values():
        pool.append(PoolItem(
            ingredient.id, Category.INGREDIENT,
            rarity=ingredient_draw_rarity,
            prize_rarity=ingredient.rarity,  # its own fc.Rarity, used only for quantity
        ))

    # Same pattern as ings
    cookie_draw_rarity = DEFAULT_RARITY_BY_CATEGORY[Category.COOKIE]
    for cookie in SPIN_COOKIES:
        pool.append(PoolItem(
            cookie["itemId"], Category.COOKIE,
            rarity=cookie_draw_rarity,
            prize_rarity=cookie["rarity"],
        ))

    for item_id in SPIN_DYES:
        pool.append(PoolItem(item_id, Category.DYE, DEFAULT_RARITY_BY_CATEGORY[Category.DYE]))

    # Home items may name their own draw rarity; the rocks do, since badges
    # count them. Everything else takes the category default.
    for home_item in SPIN_HOME_ITEMS:
        pool.append(PoolItem(
            home_item["itemId"], Category.HOME,
            rarity=home_item.get("rarity", DEFAULT_RARITY_BY_CATEGORY[Category.HOME]),
            c1=home_item["c1"], c2=home_item["c2"],
        ))

    for badge in SPIN_BADGE_IDS.values():
        pool.append(PoolItem(badge.id, Category.BADGE, badge.rarity))

    # The master pool has both genders - pool is gender-locked at spintime
    for w in SPIN_WARDROBE_FAIRIES:
        pool.append(PoolItem(
            w["itemId"], Category.WARDROBE, DEFAULT_RARITY_BY_CATEGORY[Category.WARDROBE],
            gender=Gender.FAIRY, c1=w["c1"], c2=w["c2"],
        ))
    for w in SPIN_WARDROBE_SPARROWS:
        pool.append(PoolItem(
            w["itemId"], Category.WARDROBE, DEFAULT_RARITY_BY_CATEGORY[Category.WARDROBE],
            gender=Gender.SPARROW, c1=w["c1"], c2=w["c2"],
        ))

    return pool

_MASTER_POOL = _build_master_pool()
_POOL_BY_GENDER: dict[Gender, list[PoolItem]] = {}

def _pool_for_gender(gender: Gender) -> list[PoolItem]:
    if gender not in _POOL_BY_GENDER:
        _POOL_BY_GENDER[gender] = [
            item for item in _MASTER_POOL
            if item.gender is None or item.gender == gender
        ]
    return _POOL_BY_GENDER[gender]

# ───────────────────────────────── GACHA DRAW LOGIC ───────────────────────────────── #
def draw_daily_spin(
    gender: Gender,
    excluded_badge_ids: set[int],
    excluded_categories: set[Category],
    n: int = 3,
) -> list[PoolItem]:
    """
    excluded_badge_ids: badges already earned — server-authoritative,
        we should never trust the client mask for this.
    excluded_categories: whole categories to skip (WARDROBE if wardrobe
        full, HOME if storage full) — client mask is fine to trust here,
        worst case is that a full-inventory player gets an ungrantable item.
    """
    candidates = [
        item for item in _pool_for_gender(gender)
        if item.category not in excluded_categories
        and item.id not in excluded_badge_ids
    ]
    return draw_without_replacement(candidates, n, weight_fn=lambda item: item.weight)