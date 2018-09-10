from sense_hat import SenseHat
import time

def set_message(message, background_color=(0, 0, 0), foreground_color=(255, 255, 255), speed=0.10):
    sense = SenseHat()
    sense.show_message(message, text_colour=foreground_color, back_colour=background_color, scroll_speed=speed)
