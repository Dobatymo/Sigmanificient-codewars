"""Kata url: https://www.codewars.com/kata/515e271a311df0350d00000f."""

from typing import List


def square_sum(numbers: List[int]) -> int:
    return sum(x ** 2 for x in numbers)