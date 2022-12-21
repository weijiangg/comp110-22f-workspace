"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730569555"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Return data of node at given index or raise error."""
    if head is None:
        raise IndexError("Index is out of bounds on the list")
    elif index == 0:
        return head.data
    return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Given node, returns maximun data or raises error if node empty."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.data
    else:
        max_value: int = max(head.next)
        if head.data > max_value:
            return head.data
        else:
            return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Convert a list of ints into linked list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns new linked list with values sacled by factor."""
    if head is None:
        return None
    return Node(head.data * factor, scale(head.next, factor))

