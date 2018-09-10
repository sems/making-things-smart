from sense_hat import SenseHat
import time

def set_color():
    sense = SenseHat()

    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    while True:
        sense.show_message("I you love!", text_colour=yellow, back_colour=blue, scroll_speed=0.10)
