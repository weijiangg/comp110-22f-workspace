"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730569555"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between the Point object the method was called on and some other Point object passed in as a parameter."""
        x: float = self.x - other.x
        y: float = self.y - other.y
        return sqrt(x ** 2 + y ** 2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Ticks through the cells."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() is True:
            return "red"
        elif self.is_vulnerable() is True:
            return "gray"
        elif self.is_immune() is True:
            return "green"
        else:
            return "black"

    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns true if the cells is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns True is the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, self2: Cell) -> None:
        """Method that will be called when two Cell objects do make contact."""
        if self.is_infected() is True and self2.is_vulnerable() is True:
            self2.contract_disease()
        elif self2.is_infected() is True and self.is_vulnerable() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the Cell object’s sickness attribute is equal to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    
    def __init__(self, cells: int, speed: float, start_infected: int, start_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        if start_infected >= cells:
            raise ValueError("More infected than cell count.")
        elif start_infected <= 0:
            raise ValueError("starts with less than 1 infected.")
        elif start_immune >= cells:
            raise ValueError("More immune than cell count.")
        elif start_immune < 0:
            raise ValueError("Negative number of immune cells.")
        elif start_immune + start_infected > cells:
            raise ValueError("Too many immune and infected cells.")
        for i in range(start_infected):
            self.population[i].contract_disease()
        for x in range(start_immune):
            self.population[x].immunize()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        Model.check_contacts(self)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Test whether any two Cell values come in “contact” with one another."""
        i: int = 0
        for x in range(len(self.population)):
            i = x + 1
            while i < len(self.population):
                if self.population[x].location.distance(self.population[i].location) <= constants.CELL_RADIUS:
                    self.population[x].contact_with(self.population[i])
                i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected() is True:
                return False
        return True