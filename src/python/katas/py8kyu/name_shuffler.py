"""Kata url: https://www.codewars.com/kata/559ac78160f0be07c200005a."""


def name_shuffler(str_: str) -> str:
    return ' '.join(str_.split()[::-1])