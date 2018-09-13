from colorsys import hsv_to_rgb
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

hues = [
    0.95, 0.88, 0.81, 0.74, 0.67, 0.60, 0.52, 0.45,
    0.87, 0.80, 0.73, 0.66, 0.59, 0.52, 0.45, 0.38,
    0.80, 0.73, 0.66, 0.58, 0.51, 0.44, 0.37, 0.30,
    0.72, 0.65, 0.58, 0.51, 0.44, 0.36, 0.29, 0.22,
    0.64, 0.57, 0.50, 0.43, 0.36, 0.29, 0.22, 0.15,
    0.57, 0.50, 0.42, 0.35, 0.28, 0.21, 0.14, 0.07,
    0.49, 0.42, 0.35, 0.28, 0.21, 0.13, 0.06, 0.00,
    0.41, 0.34, 0.27, 0.20, 0.13, 0.06, 0.00, 0.00,
    ]

def scale(v):
    return int(v * 255)

def proceedRainbow():
    global hues
    hues = [(h + 0.01) % 1.0 for h in hues]
    pixels = [hsv_to_rgb(h, 1.0, 1.0) for h in hues]
    pixels = [(scale(r), scale(g), scale(b)) for r, g, b in pixels]
    sense.set_pixels(pixels)
