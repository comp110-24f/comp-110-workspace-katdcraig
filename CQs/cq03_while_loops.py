"""While loop practice"""

__author__: str = "730659835"


def num_instances(phrase: str, search_char: str) -> int:
    """Checks for character in phrase"""
    index: int = 0
    instances: int = 0
    while index < len(phrase):
        # loops through phrase checking for character
        if phrase[index] == search_char:
            instances = instances + 1
        index = index + 1
    return instances


# for some reason it doesn't work when imported in REPL; returns number of letters
