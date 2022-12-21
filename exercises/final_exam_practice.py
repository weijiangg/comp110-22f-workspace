def multi(list: list[int]) -> list[bool]:
    result: list[bool] = []
    i: int = 0
    i2: int = 1
    x: int = len(list)
    x -= 1
    if (list[0] % list[x]) == 0:
        result.append(True)
    else:
         result.append(False)
    while i2 <= x:
        if (list[i2] % list[i]) == 0:
            result.append(True)
            i += 1
            i2 += 1
        else:
            result.append(False)
            i += 1
            i2 += 1
    return result

#print(multi([2, 3, 4, 8, 16, 2, 4, 2]))

def merge(list: list[str], list2: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(list) != len(list2):
        return result
    i: int = 0
    while i < len(list2):
        result[list[i]] = list2[i]
        i += 1
    return result

#print(merge(['blue', 'yellow', 'red'], [5, 2, 4]))


def reverse(input: str) -> str:
    result: str = ""
    i: int = len(input)
    i -= 1
    while i >= 0:
        result += input[i]
        i -= 1
    return result

#print(reverse("abcd"))


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += (mallows * 2)
    
    def calorie_count(self) -> float:
        calories: int = 0
        if self.flavor == "vanilla":
            calories += 30
        elif self.flavor == "peppermint":
            self.calorie_count += 30
        else:
            self.calorie_count += 20
        if self.has_whip is True:
            self.calorie_count += 100
        self.calorie_count += (self.marshmallow_count / 2)
        return self.calorie_count

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __inti__(self, name: str, purpose: str, initalminutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = initalminutes

    def add_time(self, x: int) -> None:
        self.minutes += x
    
    def reset(self) -> int:
        temp: int = self.minutes
        self.minutes = 0
        return temp

    def report(self) -> None:
        hours: int = (self.minutes // 60)
        minutes: int = (self.minutes % 60)
        print(f"{self.name} has spent {hours} hours and {minutes} minutes on {self.purpose}.")


def factorial(x: int) -> int:
    result: int = 1 
    if x == 0:
        return result
    if x == 1:
        return result
    else:
        return x * factorial(x - 1)

def reverse(list: list[int]) -> list[int]:
    i: int = len(list)
    i -= 1
    result: list[int] = []
    while i >= 0:
        result.append(list[i] * 2)
        i -= 1
    return result


def biscuit(dict: dict[str, list[int]]) -> dict[str,bool]:
    result: dict[str, bool] = {}
    for value in dict:
        total: int = 0
        for values in dict[value]:
            total += values
        if total >= 100:
            result[value] = True
        else:
            result[value] = False
    return result

#print(biscuit({ 'UNCvsDuke': [38, 20, 42] , 'UNCvsState': [9, 51, 16, 23] }))

def mult(list: list[int]) -> list[bool]:
    result: list[bool] = []
    i: int = len(list)
    i -= 1
    if (list[i] % list[0]) == 0:
        result.append(True)
    else:
        result.append(False)
    x: int = 1
    while x < len(list):
        if (list[x] % list[x - 1]) == 0:
            result.append(True)
        else:
            result.append(False)
        x += 1
    return result

#print(mult([2, 3, 4, 8, 16, 2, 4, 2]))

def merg(list: list[str], list2: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(list) != len(list2):
        return result
    i: int = 0
    while i < len(list):
        result[list[i]] = list2[i]
        i += 1
    return result

#print(merg(['blue', 'yellow', 'red'], [5, 2, 4]))

def filte(list: list[str], dict: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for value in dict:
        for values in list:
            if value == values:
                result[value] = dict[value]
    return result

print(filte(["a", "c"], {"a": 1, "b": 2, "c": 3}))  