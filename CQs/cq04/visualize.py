"""Prints concatenation from concatenation.py"""

__author__: str = "730659835"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# imports go at top

x: str = "123"
y: str = "abc"

print(concat(input1=x, input2=y))
print(get_coords(xs=x, ys=y))
# outputs results of functions
