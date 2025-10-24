"""Random helper utilities shared across notebooks."""

from __future__ import annotations

import random
from typing import List


def rand_int_array(n: int, low: int, high: int = 20) -> List[int]:
    """
    Generate an array of n random integers in [low, high].

    Args:
        n: Number of integers to generate.
        low: Inclusive lower bound for generated integers.
        high: Inclusive upper bound for generated integers. Defaults to 20.

    Returns:
        List[int]: List containing n random integers.
    """

    if low > high:
        msg = f"low ({low}) must be <= high ({high})"
        raise ValueError(msg)

    return [random.randint(low, high) for _ in range(n)]
