import os, sys, signal, subprocess
from sense_hat import SenseHat
from time import sleep

from libs.set_color import *
from libs.clear_console import *

from modes.shake import *
from modes.terminal import *
from modes.rainbow import *
from modes.circle import *
from modes.joystick import *
from modes.preset import *

import variables.colors as c
import variables.joystick as j
import variables.mode as m
import variables.console as con

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
			joystickPreset(event.direction)
	                set_color()
		elif m.mode[m.mode_index] == "joystick":
			joystickJoystick(event.direction)
            		set_color()
	elif event.action == "held" and m.mode[m.mode_index] == "joystick":
		joystickJoystickHeld(event.direction)
       	        set_color()

def joystick_move_middle(event):
	global gyroscope_check
	if event.action == "pressed":
		m.mode_index += 1
        while m.mode[m.mode_index] in m.mode_not_usable:
            if m.mode_index == len(m.mode) - 1:
                m.mode_index = 0
            else:
                m.mode_index += 1
	if m.mode[m.mode_index] == "preset":
		c.color = c.color_presets[c.color_index]
		set_color()
	elif m.mode[m.mode_index] == "joystick":
		j.joystick_index = 0
		c.color = (j.joystick_r, j.joystick_g, j.joystick_b)
		set_color()
	elif m.mode[m.mode_index] == "shake":
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
	                clear_console()
			# print(bcolors.HEADER+"Mode: "+bcolors.ENDC+`m.mode`)
                        print(bcolors.HEADER+"Mode: "+bcolors.ENDC+`m.mode[m.mode_index]`)
			print(bcolors.HEADER+"Mode index: "+bcolors.ENDC+`m.mode_index`)
			print(bcolors.OKBLUE+"Joystick R: "+bcolors.ENDC+`j.joystick_r`)
			print(bcolors.OKBLUE+"Joystick G: "+bcolors.ENDC+`j.joystick_g`)
			print(bcolors.OKBLUE+"Joystick B: "+bcolors.ENDC+`j.joystick_b`)
			print(bcolors.OKBLUE+"Joystick index: "+bcolors.ENDC+`j.joystick_index`)
			# print(bcolors.WARNING+"Color preset: "+bcolors.ENDC+`c.color_presets`)
			print(bcolors.WARNING+"Color index: "+bcolors.ENDC+`c.color_index`)
			print(bcolors.WARNING+"Color: "+bcolors.ENDC+`c.color`)
            		if m.mode[m.mode_index] == "time":
            		        print(con.sun)
		if m.mode[m.mode_index] == "shake":
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
        	elif m.mode[m.mode_index] == "circle":
        	    proceedCircle()
    		elif m.mode[m.mode_index] == "terminal":
        	    set_color_terminal()
        	    set_color()
		sleep(0.04)
