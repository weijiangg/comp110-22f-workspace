"""EX07 - Dictionary Function. Function skeletons and implementations."""

__author__ = "730569555"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dictionary with string key and string value, it will inverse the dictionary so that the value will become the key and the key will become with value."""
    values_list: list[str] = []
    for key in x:
        values_list.append(x[key])
    i: int = 0
    z: int = 1
    while i < (len(values_list)):
        while z < (len(values_list)):
            if values_list[i] == values_list[z]:
                raise KeyError
            z += 1
        i += 1
        z = (i + 1)
    result: dict[str, str] = {}
    for key in x:
        result[x[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Given a diction of names and favorite colors, it will return the color that is the most favorite."""
    i: int = 0
    list_values: list[str] = []
    for key in x:
        list_values.append(x[key])
    color_dict: dict[str, str] = {}
    while i < len(list_values):
        if list_values[i] in color_dict:
            color_dict[list_values[i]] += 1
        else:
            color_dict[list_values[i]] = 1
        i += 1
    color_values: list[int] = []
    for value in color_dict:
        color_values.append(color_dict[value])
    current_most: int = 0
    most_colors: str = ""
    i = 0
    while i < len(color_values):
        if current_most < color_values[i]:
            current_most = color_values[i]
        i += 1
    for key in color_dict:
        if color_dict[key] == current_most:
            most_colors = key
    return most_colors


def count(x: list[str]) -> dict[str, int]:
    """Given a list of strings, it will make a dictionary counting the amount of each unique key is in the list."""
    result: dict[str, str] = {}
    for item in x:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result