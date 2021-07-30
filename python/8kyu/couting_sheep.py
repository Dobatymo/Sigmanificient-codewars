"""Kata url: https://www.codewars.com/kata/54edbc7200b811e956000556."""

from typing import Optional, List


def count_sheeps(sheep: List[Optional[bool]]) -> int:
    return sum(x for x in sheep if isinstance(x, bool))
