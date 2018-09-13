import os, sys, signal, subprocess
from sense_hat import SenseHat
from time import sleep

from libs.set_color import *

import variables.colors as c

sense = SenseHat()
sense.clear()

def joystickPreset(direction):
    if direction == "up" or direction == "right":
        if c.max_color_index == c.color_index:
            c.color_index = c.min_color_index
        else:
            c.color_index += 1
    elif direction == "down" or direction == "left":
        if c.min_color_index == c.color_index:
            c.color_index = c.max_color_index
        else:
            c.color_index -= 1
    c.color = c.color_presets[c.color_index]
