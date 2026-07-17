import random
from typing import Protocol, TypeVar

T = TypeVar("T")

class Weighted(Protocol):
    weight: float

def draw_without_replacement(candidates: list[T], n: int, weight_fn) -> list[T]:
    """
    Weighted sampling without replacement (Efraimidis-Spirakis).
    weight_fn: callable that returns a positive float weight for a candidate.
    """
    if len(candidates) < n:
        raise ValueError(f"Not enough candidates: {len(candidates)} < {n}")

    keyed = [
        (random.random() ** (1.0 / weight_fn(item)), item)
        for item in candidates
    ]
    keyed.sort(key=lambda pair: pair[0], reverse=True)
    return [item for _, item in keyed[:n]]