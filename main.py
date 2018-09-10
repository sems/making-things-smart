import signal
from sense_hat import SenseHat
from time import sleep
from set_color import set_color

sense = SenseHat()
sense.clear()

white = (255,255,255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
brown = (165, 42, 42)
grey = (190, 190, 190)

color_presets = [white, red, green, blue, orange, yellow, cyan, magenta, brown, grey]

# Functions ----------------
def joystick_move_up(event):
	sense.clear()
def joystick_move_down(event):
	sense.clear()
def joystick_move_left(event):
	sense.clear()
def joystick_move_right(event):
	sense.clear()
def joystick_move_middle(event):
	sense.clear()

def clear():
	sense.clear()

def exit(signal, frame):
	clear()
	print("Bye!")
	sys.exit(0)

set_color()

# Main program -------------
if __name__ == '__init__':
	sense.stick.direction_up = joystick_move_up
	sense.stick.direction_down = joystick_move_down
	sense.stick.direction_left = joystick_move_left
	sense.stick.direction_right = joystick_move_right
	sense.stick.direction_middle = joystick_move_middle


	signal.signal(signal.SIGING, exit)
