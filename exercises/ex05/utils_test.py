"""Utils test functions."""

__author__ = "730569555"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens1() -> None:
    """Tests if the list 1, 2, 3, will return only the even values."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens2() -> None:
    """Tests if the list 4, 5, 6, 7 will return only the even values."""
    xs: list[int] = [4, 5, 6, 7]
    assert only_evens(xs) == [4, 6]


def test_only_evens3() -> None:
    """Tests if the list 7, 11, 13, will return an empty list."""
    xs: list[int] = [7, 11, 13]
    assert only_evens(xs) == []


def test_concat1() -> None:
    """Tests given 2 lists, it was concat them together."""
    xs1: list[int] = [0, 0, 0]
    xs2: list[int] = [5, 5, 5]
    assert concat(xs1, xs2) == [0, 0, 0, 5, 5, 5]


def test_concat2() -> None:
    """Tests given 2 lists, it was concat them together."""
    xs1: list[int] = [0, 1, 2]
    xs2: list[int] = [3, 4, 5]
    assert concat(xs1, xs2) == [0, 1, 2, 3, 4, 5]


def test_concat3() -> None:
    """Tests given 2 lists, it was concat them together."""
    xs1: list[int] = []
    xs2: list[int] = []
    assert concat(xs1, xs2) == []


def test_sub1() -> None:
    """Tests that gives 2 integers and a list of integers, it return a list with the integers between the 2 index numbers given."""
    xs: list[int] = [10, 20, 30, 40]
    x1: int = 1
    x2: int = 3
    assert sub(xs, x1, x2) == [20, 30]


def test_sub2() -> None:
    """Tests that gives 2 integers and a list of integers, it return a list with the integers between the 2 index numbers given."""
    xs: list[int] = [10, 20, 30, 40]
    x1: int = -1
    x2: int = 3
    assert sub(xs, x1, x2) == [10, 20, 30]


def test_sub3() -> None:
    """Tests that gives 2 integers and a list of integers, it return a list with the integers between the 2 index numbers given."""
    xs: list[int] = [10, 20, 30, 40]
    x1: int = 1
    x2: int = 9
    assert sub(xs, x1, x2) == [20, 30, 40]