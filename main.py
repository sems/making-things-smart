import os, sys, signal
from sense_hat import SenseHat
from time import sleep
from set_color import set_color
from set_message import set_message
<<<<<<< HEAD
=======
import colors
>>>>>>> 7834e6c4faaf610dd8e34344fae006230763c401

sense = SenseHat()
sense.clear()

mode = ["preset", "joystick", "gyroscope", "voice"]
mode_index = 0

joystick_r = 255
joystick_g = 255
joystick_b = 255
joystick_index = 0

# Functions ----------------
def joystick_move_up(event):
	global mode
	global mode_index
	global joystick_r
	global joystick_g
	global joystick_b
	global joystick_index
	if mode[mode_index] == "preset":
		colors.color_index += 1
		colors.color = colors.color_presets[colors.color_index]
		# set_color.py
	if mode[mode_index] == "joystick":
		if joystick_index == 0:
			joystick_r += 1
		if joystick_index == 1:
			joystick_g += 1
		if joystick_index == 2:
			joystick_b += 1
def joystick_move_down(event):
	global mode
	global mode_index
	global joystick_r
	global joystick_g
	global joystick_b
	global joystick_index
	if mode[mode_index] == "preset":
		colors.color_index -= 1
		colors.color = colors.color_presets[colors.color_index]
		# set_color.py
	if mode[mode_index] == "joystick":
		if joystick_index == 0:
			joystick_r -= 1
		if joystick_index == 1:
			joystick_g -= 1
		if joystick_index == 2:
			joystick_b -= 1
def joystick_move_left(event):
	global mode
	global mode_index
	global joystick_index
	if mode[mode_index] == "preset":
		colors.color_index -= 1
		colors.color = colors.color_presets[colors.color_index]
		# set_color.py
	if mode[mode_index] == "joystick":
		if joystick_index == 0:
			joystick_index = 2
		else:
			joystick_index -= 1
def joystick_move_right(event):
	global mode
	global mode_index
	global joystick_index
	if mode[mode_index] == "preset":
		colors.color_index += 1
		colors.color = colors.color_presets[colors.color_index]
		# set_color.py
	if mode[mode_index] == "joystick":
		if joystick_index == 2:
			joystick_index = 0
		else:
			joystick_index += 1
def joystick_move_middle(event):
	global mode
	global mode_index
	if event.action == "pressed":
		mode_index += 1
		if mode[mode_index] == "gyroscope" or mode[mode_index] == "voice":
			mode_index = 0

def clear():
	sense.clear()

def exit(signal, frame):
	clear()
	print("Bye!")
	sys.exit(0)

set_color()

# Main program -------------
if __name__ == '__main__':
	sense.stick.direction_up = joystick_move_up
	sense.stick.direction_down = joystick_move_down
	sense.stick.direction_left = joystick_move_left
	sense.stick.direction_right = joystick_move_right
	sense.stick.direction_middle = joystick_move_middle


	signal.signal(signal.SIGINT, exit)
	while True:
		print("Mode: "+`mode`)
		print("Mode index: "+`mode_index`)
		print("Joystick R: "+`joystick_r`)
		print("Joystick G: "+`joystick_g`)
		print("Joystick B: "+`joystick_b`)
		print("Joystick index: "+`joystick_index`)
		print("Color preset: "+`colors.color_presets`)
		print("Color index: "+`colors.color_index`)
		print("Color: "+`colors.color`)
		sleep(1)
