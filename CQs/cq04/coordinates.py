"""Prints pairs of characters in strings"""

__author__: str = "730659835"


def get_coords(xs: str, ys: str) -> None:
    """Makes coordinates from 2 strings"""
    ind_xs: int = 0
    while ind_xs < len(xs):
        # monitors xs string and increases index by 1 each loop
        ind_ys: int = 0
        while ind_ys < len(ys):
            # monitors ys string and increases index by 1 each loop
            print(f"({xs[ind_xs]}, {ys[ind_ys]})")
            # prints set of coordinates for each loop
            ind_ys += 1
        ind_xs += 1
