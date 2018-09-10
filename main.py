import os, sys, signal
from sense_hat import SenseHat
from time import sleep
from set_color import set_color
from set_message import set_message
import colors as c
import joystick as j

sense = SenseHat()
sense.clear()

mode = ["preset", "joystick", "gyroscope", "voice", "time"]
mode_index = 0

# Functions ----------------
def joystick_move(event):
	global mode, mode_index
	if event.action == "pressed":
		if mode[mode_index] == "preset":
			if event.direction == "up" or event.direction == "right":
				if c.max_color_index == c.color_index:
					c.color_index = c.min_color_index
				else:
					c.color_index += 1
			elif event.direction == "down" or event.direction == "left":
				if c.min_color_index == c.color_index:
					c.color_index = c.max_color_index
				else:
					c.color_index -= 1
			c.color = c.color_presets[c.color_index]
			# set_color.py
		elif mode[mode_index] == "joystick":
			if event.direction == "up":
				if j.joystick_index == 0:
					j.joystick_r += 1
				if j.joystick_index == 1:
					j.joystick_g += 1
				if j.joystick_index == 2:
					j.joystick_b += 1
			elif event.direction == "down":
				if j.joystick_index == 0:
					j.joystick_r -= 1
				if j.joystick_index == 1:
					j.joystick_g -= 1
				if j.joystick_index == 2:
					j.joystick_b -= 1
			elif event.direction == "left":
				if j.joystick_index == 0:
					j.joystick_index = 2
				else:
					j.joystick_index -= 1
			elif event.direction == "right":
				if j.joystick_index == 2:
					j.joystick_index = 0
				else:
					j.joystick_index += 1
	set_color()
def joystick_move_middle(event):
	global mode, mode_index
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

# Main program -------------
if __name__ == '__main__':
	sense.stick.direction_up = joystick_move_up
	sense.stick.direction_down = joystick_move_down
	sense.stick.direction_left = joystick_move_left
	sense.stick.direction_right = joystick_move_right
	sense.stick.direction_middle = joystick_move_middle

	c.color_count = len(c.color_presets)
	c.max_color_index = c.color_count - 1
	c.min_color_index = 0
	set_color()

	signal.signal(signal.SIGINT, exit)
	while True:
		print("Mode: "+`mode`)
		print("Mode index: "+`mode_index`)
		print("Joystick R: "+`j.joystick_r`)
		print("Joystick G: "+`j.joystick_g`)
		print("Joystick B: "+`j.joystick_b`)
		print("Joystick index: "+`j.joystick_index`)
		print("Color preset: "+`c.color_presets`)
		print("Color index: "+`c.color_index`)
		print("Color: "+`c.color`)
		sleep(0.05)
