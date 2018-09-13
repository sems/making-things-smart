import os, sys, signal, subprocess
from sense_hat import SenseHat
from time import sleep

from libs.set_color import *

from modes.gyroscope import *
from modes.terminal import *
from modes.rainbow import *

import variables.colors as c
import variables.joystick as j
import variables.mode as m

sense = SenseHat()
sense.clear()

tempDebug = True

# Classes ------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Functions ----------------
def joystick_move(event):
	if event.action == "pressed":
		if m.mode[m.mode_index] == "preset":
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
		elif m.mode[m.mode_index] == "joystick":
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
	elif event.action == "held" and m.mode[m.mode_index] == "joystick":
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
	global gyroscope_check
	if event.action == "pressed":
		m.mode_index += 1
		if m.mode[m.mode_index] == "voice" or m.mode[m.mode_index] == "music":
			m.mode_index = 0
		if m.mode[m.mode_index] == "preset":
			c.color = c.color_presets[c.color_index]
			set_color()
		elif m.mode[m.mode_index] == "joystick":
			j.joystick_index = 0
			c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
			set_color()
		elif m.mode[m.mode_index] == "gyroscope":
			set_random_gyroscope_color()
		elif m.mode[m.mode_index] == "time":
			try:
				execfile('modes/sun.py')
			except SystemExit as e:
				if e.code == 255:
					if tempDebug:
						print(bcolors.ERROR+"sys.exit was called within sun.py"+bcolors.ENDC)
				else:
					sys.exit()

def clear():
	sense.clear()

def exit(signal, frame):
	m.mode_index = 0
	clear()
	print(bcolors.OKGREEN+"Bye!"+bcolors.ENDC)
	sys.exit(0)

# Main program -------------
if __name__ == '__main__':
	if tempDebug:
		print("Colors:")
		print(bcolors.HEADER + "Header" + bcolors.ENDC)
		print(bcolors.OKBLUE + "OKBlue" + bcolors.ENDC)
		print(bcolors.OKGREEN + "OKGreen" + bcolors.ENDC)
		print(bcolors.WARNING + "Warning" + bcolors.ENDC)
		print(bcolors.ERROR + "Error" + bcolors.ENDC)
		print(bcolors.BOLD + "Bold" + bcolors.ENDC)
		print(bcolors.UNDERLINE + "Underline" + bcolors.ENDC)

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
		if tempDebug:
			print(bcolors.HEADER+"Mode: "+bcolors.ENDC+`m.mode`)
			print(bcolors.HEADER+"Mode index: "+bcolors.ENDC+`m.mode_index`)
			print(bcolors.OKBLUE+"Joystick R: "+bcolors.ENDC+`j.joystick_r`)
			print(bcolors.OKBLUE+"Joystick G: "+bcolors.ENDC+`j.joystick_g`)
			print(bcolors.OKBLUE+"Joystick B: "+bcolors.ENDC+`j.joystick_b`)
			print(bcolors.OKBLUE+"Joystick index: "+bcolors.ENDC+`j.joystick_index`)
			print(bcolors.WARNING+"Color preset: "+bcolors.ENDC+`c.color_presets`)
			print(bcolors.WARNING+"Color index: "+bcolors.ENDC+`c.color_index`)
			print(bcolors.WARNING+"Color: "+bcolors.ENDC+`c.color`)
		if m.mode[m.mode_index] == "gyroscope":
			set_random_gyroscope_color()
			set_color()
		elif m.mode[m.mode_index] == "time":
			try:
				execfile('modes/sun.py')
			except SystemExit as e:
				if e.code == 255:
					if tempDebug:
						print(bcolors.ERROR+"sys.exit was called within sun.py"+bcolors.ENDC)
				else:
					sys.exit()
		elif m.mode[m.mode_index] == "rainbow":
            proceedRainbow()
		sleep(0.04)
