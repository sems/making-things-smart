from sense_hat import SenseHat
import time
import random
import variables.colors as c

def set_random_gyroscope_color():
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
        c.color = x
        return new_color
