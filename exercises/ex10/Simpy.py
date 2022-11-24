"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730569555"


class Simpy:
    """Simpy Class."""
    values: float[list]

    def __init__(self, x: list[float]) -> None:
        """Init method."""
        self.values = x

    def __repr__(self) -> str:
        """Returns string of values."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fills values with an int."""
        self.values = []
        for _ in range(y):
            self.values.append(x)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a list with values that increase or decrease."""
        assert step != 0.0
        self.values = []
        x: float = start
        if x >= 0.0:
            while x < stop:
                self.values.append(x)
                x += step
        if x < 0.0:
            while x > stop:
                self.values.append(x)
                x += step
    
    def sum(self) -> float:
        """Sums that values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Mask methods that adds."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in range(len(self.values)):
                result.values.append(self.values[value] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Power method that uses power on numbers."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in range(len(self.values)):
                result.values.append(self.values[value] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Gives list of true or false if numbers match."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in range(len(self.values)):
                if self.values[value] == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Gives list of true or false if number is greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in range(len(self.values)):
                if self.values[value] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloading subscription notation."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
            return result
        else:
            i: int = 0
            result: Simpy = Simpy([])
            while i < len(rhs):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result