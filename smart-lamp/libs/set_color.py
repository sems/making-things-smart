from sense_hat import SenseHat
import time
import random
import variables.colors as c

def set_color():
    sense = SenseHat()

    # old_color_index = c.color_presets.index(old_color)
    x = c.color

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

    try:
        sense.set_pixels(new_color)
    except:
        print("Error while setting pixels")

    return new_color
