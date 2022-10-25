"""EX07 - Dictionary test functions."""

__author__ = "730569555"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert1() -> None:
    """Given 5 names in a dictionary, it returns a dictionary with the last name then first name."""
    x: dict[str, str] = {'kris': 'jordan', 'michael': 'jordann', 'wei': 'jiang', 'weii': 'jiangg', 'weiii': 'jianggg'}
    assert invert(x) == {'jordan': 'kris', 'jordann': 'michael', 'jiang': 'wei', 'jiangg': 'weii', 'jianggg': 'weiii'}


def test_invert2() -> None:
    """Give a dictionary of letters, it returns the inverse dictionary."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(x) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert3() -> None:
    """(Edge Case) Given a dictionary with key and value."""
    x: dict[str, str] = {'1': '2'}
    assert invert(x) == {'2': '1'}


def test_favorite_color1() -> None:
    """Given a dictionary of people's color, it will return the most common color."""
    x: dict[str, str] = {'person1': 'blue', 'person2': 'red', 'person3': 'green', 'person4': 'red'}
    assert favorite_color(x) == "red"


def test_favorite_color2() -> None:
    """(Edge Case) Given a dictionary of people's color with a tie, it will return the first color."""
    x: dict[str, str] = {'person1': 'blue', 'person2': 'blue', 'person3': 'green', 'person4': 'green'}
    assert favorite_color(x) == "green"


def test_favorite_color3() -> None:
    """Given a dictionary of people's color, it will return the most common color."""
    x: dict[str, str] = {'joe': 'purple', 'bob': 'red', 'kevin': 'white', 'kris': 'yellow', 'emma': 'purple'}
    assert favorite_color(x) == "purple"


def test_count1() -> None:
    """Given a list of colors, return a dictionary the counts the amount of each color."""
    x: list[str] = ['green', 'blue', 'green', 'black', 'yellow', 'red']
    assert count(x) == {'green': 2, 'blue': 1, 'black': 1, 'yellow': 1, 'red': 1}


def test_count2() -> None:
    """(Edge case) Given a list of only 1 type value, return the count of that value."""
    x: list[str] = ['comp', 'comp', 'comp', 'comp', 'comp', 'comp']
    assert count(x) == {'comp': 6}


def test_count3() -> None:
    """Given of list of days, return the count of each."""
    x: list[str] = ['monday', 'sunday', 'monday', 'friday', 'mondayp', 'thrusday', 'sunday']
    assert count(x) == {'monday': 2, 'sunday': 2, 'friday': 1, 'mondayp': 1, 'thrusday': 1}