import signal
from sense_hat import SenseHat
from time from sleep

sense = SenseHat()
sense.clear()

white = (255,255,255)
blue = (0, 0, 255)

# Functions ----------------
def joystick_move_up(event):
	sense.clear()
def joystick_move_down(event):
	sense.clear()
def joystick_move_left(event):
	sense.clear()
def joystick_move_right(event):
	sense.clear()
def joystick_move_click(event):
	sense.clear()

def clear():
	sense.clear()

def exit(signal, frame):
	clear()
	print("Bye!")
	sys.exit(0)

# Main program -------------
if __name__ == '__init__':
	sense.stick.direction_up = joystick_move_up
	sense.stick.direction_down = joystick_move_down
	sense.stick.direction_left = joystick_move_left
	sense.stick.direction_right = joystick_move_right

	signal.signal(signal.SIGING, exit)
