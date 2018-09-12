#!/usr/bin/python3
import os, sys, signal
import datetime
from sense_hat import SenseHat

print("Content-type: text/plain\n")

print("een python CGI script");
print(datetime.datetime.now())

print("Einde script")

sense = SenseHat()
sense.clear([255, 255, 255])

# Arguments
verbose = False
message = None

# Functions
def main():
    sense = SenseHat()
    if len(sys.argv) > 1:
        while True:
            x = sys.argv[1]

            new_color = [
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, x
            ]

            sense.set_pixels(new_color)


# Parse arguments
"""
try:
    opts, args = getopt.getopt(sys.argv[1:], "vt:T:")
except getopt.GetoptError as err:
	print(str(err))
	print('web_interface.py -v')
	print('-v: be verbose')
	sys.exit(2)

for opt, arg in opts:
    if opt == '-v':
        verbose = True
    elif opt == '-m':
        message = arg
"""

# Main program
if __name__ == "__main__":
    main()
