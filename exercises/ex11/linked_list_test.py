"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730569555"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Returns data at given Node."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_max1() -> None:
    """Max of list returns max value."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max2() -> None:
    """Max of empty list returns error."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify1() -> None:
    """Returns linkedlist from values."""
    linked_list = Node(10, Node(20, Node(30, Node)))
    assert str(linkify([10, 20, 30])) == str(linked_list)


def test_linkify2() -> None:
    """Returns empty list."""
    assert linkify([]) is None


def test_scale1() -> None:
    """Returns link list from given values."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert str(scale(linked_list, 2)) == str(linkify([20, 40, 60]))


def test_scale2() -> None:
    """Returns empty list with None."""
    assert scale(None, 2) is None
