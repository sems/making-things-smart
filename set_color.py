from sense_hat import SenseHat
import time
import random
import colors as c

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

    sense.set_pixels(new_color)

    return new_color

def set_random_color():
    sense = SenseHat()

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        x = random.choice(c.color_presets)
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
    
