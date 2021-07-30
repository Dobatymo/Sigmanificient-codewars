"""Kata url: https://www.codewars.com/kata/559d2284b5bb6799e9000047."""

from typing import List


def add_length(str_: str) -> List[str]:
    return [f"{x} {len(x)}" for x in str_.split()]
