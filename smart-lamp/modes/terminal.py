#!/use/bin/python
import sys
from sense_hat import SenseHat
import variables.colors as c
import variables.mode as m
from libs.set_color import *


def set_color_terminal():
    sense = SenseHat()

    try:
        color = input("Type an rgb color: ")
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    except:
        print("Changed mode...")

    try:
        if color == "close" or color == "next":
            m.mode_index += 1
        else:
            c.color = color
            set_color()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    except:
        print("Not a valid input, use it as following: <number>,<number>,<number> -> 255,255,255")
