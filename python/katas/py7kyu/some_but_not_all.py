"""Kata url: https://www.codewars.com/kata/60dda5a66c4cf90026256b75."""

from typing import Any, Callable, Union, List


def some_but_not_all(seq: Union[str, List[int]], pred: Callable[[Any], Any]):
    return 0 < sum(pred(x) for x in seq) < len(seq)
