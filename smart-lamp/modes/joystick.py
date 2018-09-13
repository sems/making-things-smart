import os, sys, signal, subprocess
from sense_hat import SenseHat
from time import sleep

from libs.set_color import *

import variables.colors as c
import variables.joystick as j

sense = SenseHat()
sense.clear()

def joystickJoystick(direction):
    if direction == "up":
        if j.joystick_index == 0:
            if j.joystick_r == 255:
                j.joystick_r = 0
            else:
                j.joystick_r += 1
        if j.joystick_index == 1:
            if j.joystick_g == 255:
                j.joystick_g = 0
            else:
                j.joystick_g += 1
        if j.joystick_index == 2:
            if j.joystick_b == 255:
                j.joystick_b = 0
            else:
                j.joystick_b += 1
    elif direction == "down":
        if j.joystick_index == 0:
            if j.joystick_r == 0:
                j.joystick_r = 255
            else:
                j.joystick_r -= 1
        if j.joystick_index == 1:
            if j.joystick_g == 0:
                j.joystick_g = 255
            else:
                j.joystick_g -= 1
        if j.joystick_index == 2:
            if j.joystick_b == 0:
                j.joystick_b = 255
            else:
                j.joystick_b -= 1
    elif direction == "left":
        if j.joystick_index == 0:
            j.joystick_index = 2
        else:
            j.joystick_index -= 1
    elif direction == "right":
        if j.joystick_index == 2:
            j.joystick_index = 0
        else:
            j.joystick_index += 1
    c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
def joystickJoystickHeld(direction):
    if direction == "up":
        if j.joystick_index == 0:
            if j.joystick_r == 255:
                j.joystick_r = 0
            else:
                j.joystick_r += 1
        if j.joystick_index == 1:
            if j.joystick_g == 255:
                j.joystick_g = 0
            else:
                j.joystick_g += 1
        if j.joystick_index == 2:
            if j.joystick_b == 255:
                j.joystick_b = 0
            else:
                j.joystick_b += 1
    elif direction == "down":
        if j.joystick_index == 0:
            if j.joystick_r == 0:
                j.joystick_r = 255
            else:
                j.joystick_r -= 1
        if j.joystick_index == 1:
            if j.joystick_g == 0:
                j.joystick_g = 255
            else:
                j.joystick_g -= 1
        if j.joystick_index == 2:
            if j.joystick_b == 0:
                j.joystick_b = 255
            else:
                j.joystick_b -= 1
    c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
