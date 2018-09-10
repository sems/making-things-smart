from sense_hat import SenseHat
import time
import random
import colors


def set_color(old_color):
    sense = SenseHat()

    # x = random.choice(colors.color_presets)
    old_color_index = colors.color_presets.index(old_color)
    x = colors.color_presets[old_color_index + 1]
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

    return new_color
