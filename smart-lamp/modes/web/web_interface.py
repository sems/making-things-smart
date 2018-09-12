#!/usr/bin/python3
import os, sys, signal
import datetime
import variables.colors as c

print("Content-type: text/plain\n")

print("een python CGI script");
print(datetime.datetime.now())

print("Einde script")

# Arguments
verbose = False
message = None

# Functions
def main():
    sense = SenseHat()
    if len(sys.argv) > 1:
        while True:
            x = sys.argv[1]
            c.color = x


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
