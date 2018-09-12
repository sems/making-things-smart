from sense_hat import SenseHat
import time
import datetime
import requests
import json
import dateutil.parser
import pytz

sense = SenseHat()

white = (255, 255, 255)
orange_hues = [(246,120,88), (247,133,104), (248,147,121), (249,160,138), (250,174,155), (250,187,171), (251,201,188), (252,214,205), (253,228,222), (254,241,238)]
orange = (245, 106, 71)

zwolle = "https://api.sunrise-sunset.org/json?lat=52.5055809&lng=6.0905981&date=today&formatted=0"
sydney = "https://api.sunrise-sunset.org/json?lat=-33.8688197&lng=151.2092955&date=today&formatted=0"
san = "https://api.sunrise-sunset.org/json?lat=37.7749295&lng=-122.4194155&date=today&formatted=0"

try:
    r = requests.get(zwolle)
except:
    print("Error when getting request!")
    sys.exit(255)
parsed = json.loads(r.content)
results = parsed['results']
#print formated json data
print(json.dumps(parsed, indent=4, sort_keys=True)) ## Comment this line

# Functions
# @staticmethod
def toDataTime(datestring):
    parsed = dateutil.parser.parse(datestring) # ISO 8601 basic format
    return parsed

# Format data to proper types
sunrise = toDataTime(results['sunrise'])
sunrise_unix = time.mktime(sunrise.timetuple())

sunset = toDataTime(results['sunset'])
sunset_unix = time.mktime(sunset.timetuple())

civil_twilight_begin = toDataTime(results['civil_twilight_begin'])
civil_twilight_begin_unix = time.mktime(civil_twilight_begin.timetuple())

civil_twilight_end = toDataTime(results['civil_twilight_end'])
civil_twilight_end_unix = time.mktime(civil_twilight_end.timetuple())

utc = datetime.datetime.utcnow()

# utc = "2018-09-12 04:58:14.495419"
utc_unix = time.mktime(utc.timetuple())
utc_unix = 1536773235.0
print civil_twilight_end_unix
if sunrise_unix <= utc_unix <= sunset_unix:
    print("Het is dag")
    sense.clear(white)
else:
    # morning
    if civil_twilight_begin_unix <= utc_unix <= sunrise_unix:
        dif_sunrise = (sunrise_unix - civil_twilight_begin_unix) / 10
        print dif_sunrise
        interval_1 = civil_twilight_begin_unix + dif_sunrise

        if civil_twilight_begin_unix <= utc_unix <= (civil_twilight_begin_unix + dif_sunrise):
            sense.clear(orange01)
            print("1")
            
        for x in range(1, 10):
            if (civil_twilight_begin_unix + (dif_sunrise * x)) <= utc_unix <= (civil_twilight_begin_unix + (dif_sunrise * (x+1))):
                sense.clear(orange_hues[x])
                print(x)
                break

        #sense.clear(255,0,255)
        # print("Sleepy sleepy, need to go to bed soon!")

    #evening
    if sunset_unix <= utc_unix <= civil_twilight_end_unix:
        dif_sunset = (civil_twilight_end_unix - sunset_unix) / 10
        
        if sunset_unix <= utc_unix <= (sunset_unix + dif_sunset):
            sense.clear(orange10)
            print("10")

        for x in range(9, 0, -1):
            print x
            if (sunset_unix + (dif_sunset * x)) <= utc_unix <= (sunset_unix + (dif_sunset * (x+1))):
                sense.clear(orange_hues[x])
                print(x)
                break
    #print("Nighty night, sleep well!")
    #sense.clear(orange)
