from colorsys import hsv_to_rgb
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

hues = [0.60, 0.50, 0.40, 0.30, 0.30, 0.40, 0.50, 0.60,
        0.50, 0.40, 0.30, 0.20, 0.20, 0.30, 0.40, 0.50,
        0.40, 0.30, 0.20, 0.10, 0.10, 0.20, 0.30, 0.40,
        0.30, 0.20, 0.10, 0.00, 0.00, 0.10, 0.20, 0.30,
        0.30, 0.20, 0.10, 0.00, 0.00, 0.10, 0.20, 0.30,
        0.40, 0.30, 0.20, 0.10, 0.10, 0.20, 0.30, 0.40,
        0.50, 0.40, 0.30, 0.20, 0.20, 0.30, 0.40, 0.50,
        0.60, 0.50, 0.40, 0.30, 0.30, 0.40, 0.50, 0.60]

def scale(v):
    return int(v * 255)

while True:
    hues = [(h - 0.01) % 1.0 for h in hues]
    pixels = [hsv_to_rgb(h, 1.0, 1.0) for h in hues]
    pixels = [(scale(r), scale(g), scale(b)) for r, g, b in pixels]
    sense.set_pixels(pixels)
    sleep(0.04)
