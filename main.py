import os, sys, signal
from sense_hat import SenseHat
from time import sleep
from set_color import *
from set_message import set_message
import colors as c
import joystick as j

sense = SenseHat()
sense.clear()

mode = ["preset", "joystick", "gyroscope", "voice", "time"]
mode_index = 0

gyroscope_check = False

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
		elif mode[mode_index] == "joystick":
			if event.direction == "up":
				if j.joystick_index == 0:
					if j.joystick_r == 255:
						j.joystick_r = 0
					else:
						j.joystick_r += 1
				if j.joystick_index == 1:
					if j.joystick_g == 255:
						j.joystick_g = 0
					else:
						j.joystick_g += 1
				if j.joystick_index == 2:
					if j.joystick_b == 255:
						j.joystick_b = 0
					else:
						j.joystick_b += 1
			elif event.direction == "down":
				if j.joystick_index == 0:
					if j.joystick_r == 0:
						j.joystick_r = 255
					else:
						j.joystick_r -= 1
				if j.joystick_index == 1:
					if j.joystick_g == 0:
						j.joystick_g = 255
					else:
						j.joystick_g -= 1
				if j.joystick_index == 2:
					if j.joystick_b == 0:
						j.joystick_b = 255
					else:
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
			c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
	elif event.action == "held" and mode[mode_index] == "joystick":
		if event.direction == "up":
			if j.joystick_index == 0:
				if j.joystick_r == 255:
					j.joystick_r = 0
				else:
					j.joystick_r += 1
			if j.joystick_index == 1:
				if j.joystick_g == 255:
					j.joystick_g = 0
				else:
					j.joystick_g += 1
			if j.joystick_index == 2:
				if j.joystick_b == 255:
					j.joystick_b = 0
				else:
					j.joystick_b += 1
		elif event.direction == "down":
			if j.joystick_index == 0:
				if j.joystick_r == 0:
					j.joystick_r = 255
				else:
					j.joystick_r -= 1
			if j.joystick_index == 1:
				if j.joystick_g == 0:
					j.joystick_g = 255
				else:
					j.joystick_g -= 1
			if j.joystick_index == 2:
				if j.joystick_b == 0:
					j.joystick_b = 255
				else:
					j.joystick_b -= 1
		c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
	set_color()
def joystick_move_middle(event):
	global mode, mode_index, gyroscope_check
	if event.action == "pressed":
		mode_index += 1
		if mode[mode_index] == "time" or mode[mode_index] == "voice":
			mode_index = 0
		if mode[mode_index] == "preset":
			c.color = c.color_presets[c.color_index]
			set_color()
		elif mode[mode_index] == "joystick":
			j.joystick_index = 0
			c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
			set_color()
		elif mode[mode_index] == "gyroscope":
			gyroscope_check = True

def clear():
	sense.clear()

def exit(signal, frame):
	clear()
	print("Bye!")
	sys.exit(0)

# Main program -------------
if __name__ == '__main__':
	sense.stick.direction_up = joystick_move
	sense.stick.direction_down = joystick_move
	sense.stick.direction_left = joystick_move
	sense.stick.direction_right = joystick_move
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
		if gyroscope_check == True:
			set_random_gyroscope_color()
		sleep(0.05)
