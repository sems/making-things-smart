from sense_hat import SenseHat
import time
import datetime
import requests
import json
import dateutil.parser
import pytz

sense = SenseHat()

white = (255, 255, 255)
orange = (245, 106, 71)

zwolle = "https://api.sunrise-sunset.org/json?lat=52.5055809&lng=6.0905981&date=today&formatted=0"
sydney = "https://api.sunrise-sunset.org/json?lat=-33.8688197&lng=151.2092955&date=today&formatted=0"
san = "https://api.sunrise-sunset.org/json?lat=37.7749295&lng=-122.4194155&date=today&formatted=0"

r = requests.get(zwolle)
parsed = json.loads(r.content)
results = parsed['results']
print(json.dumps(parsed, indent=4, sort_keys=True))

def toDataTime(datestring):
    parsed = dateutil.parser.parse(datestring) # ISO 8601 basic format
    return parsed

sunrise = toDataTime(results['sunrise'])
sunriseUnix = time.mktime(sunrise.timetuple())

utc = datetime.datetime.utcnow()
utcUnix = time.mktime(utc.timetuple())

if utcUnix > sunriseUnix:
    print("De zon is al op")
    sense.clear(white)
else:
    print("De zon is nog onder")
    sense.clear(orange)