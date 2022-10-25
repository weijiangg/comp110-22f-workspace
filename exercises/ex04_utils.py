"""EX04 Lists Utility Functions."""

__author__ = "730569555"


def all(lists: list[int], x: int) -> bool:
    """First checks if the list is not empty. Checks if x equals the first number in the list and keeps going until it goes through all the numbers. If it finds that one number does not match, it returns False if it goes thought all the numbers, then it returns True."""
    if len(lists) == 0:
        return False
    i: int = 0
    while i < len(lists):
        if x == lists[i]:
            i += 1
        else:
            return False
    return True


def max(lists: list[int]) -> int:
    """First checks to see if the list is not empty, raises error if empty. Sets the higher variable as the first number, goes through each number and if it is higher than the "higher" number then it replaces it. Goes until it goes through all numbers in the list."""
    if len(lists) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    higher: int = lists[0]
    while i < len(lists):
        if lists[i] > higher:
            higher = lists[i]
            i += 1
        else:
            i += 1
    return higher


def is_equal(lists1: list[int], lists2: list[int]) -> bool:
    """First checks the length of both list is the same. Checks the 1st number of each list to see if it is the same, if not it will return False. Goes through all numbers in both lists and returns True if they all match."""
    if len(lists1) != len(lists2):
        return False
    i: int = 0
    while i < len(lists1):
        if lists1[i] != lists2[i]:
            return False
        else:
            i += 1
    return True
