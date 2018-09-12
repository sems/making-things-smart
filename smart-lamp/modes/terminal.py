#!/use/bin/python
import sys
from sense_hat import SenseHat
from variables.colors import *


def set_color_terminal():
    sense = SenseHat()

    color = input("Type an rgb color: ")

    x = color

    new_color = [
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x
    ]

    sense.set_pixels(new_color)
