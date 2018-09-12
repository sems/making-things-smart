from sense_hat import SenseHat
from colorsys import hsv_to_rgb
from time import sleep
sense = SenseHat()
sense.clear()

hues = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    ]

def scale(v):
    return int(v * 255)

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    if 1 < pitch < 179:
        hues = [(h - 0.01) % 1.0 for h in hues]
    elif 359 > pitch > 181:
        [(h + 0.01) % 1.0 for h in hues]
    if 1 < roll < 179:
        hues = [(h + 0.01) % 1.0 for h in hues]
    elif 359 > roll > 181:
        [(h - 0.01) % 1.0 for h in hues]
    pixels = [hsv_to_rgb(h, 1.0, 1.0) for h in hues]
    pixels = [(scale(r), scale(g), scale(b)) for r, g, b in pixels]
    sense.set_pixels(pixels)
    sleep(0.04)

