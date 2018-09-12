#!/use/bin/python
import sys
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255, 255, 255)

def main():
    if len(sys.argv) > 1:
        while True:
            msg = argv[1]
            sense.clear(msg)

if __name__=="__main__":
    main()
