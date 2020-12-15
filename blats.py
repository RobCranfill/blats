"""
  Back Light According To Sun
  Set the LCD's backlight according to the current sun state.
  robcranfill@gmail.com
"""
from datetime import datetime
from rpi_backlight import Backlight
from suntime import Sun, SunTimeException
import sys
import pytz

TEST = False
BACKLIGHT_DAY   = 0.75
BACKLIGHT_NIGHT = 0.25

# Seattle is 47.6062° N, 122.3321° W
LATITUDE  =   47.6062
LONGITUDE = -122.3321

# Get today's sunrise and sunset times.
def getRiseAndSet(latitude, longitude):
    sun = Sun(latitude, longitude)
    today_sr = sun.get_local_sunrise_time()
    today_ss = sun.get_local_sunset_time()
    if TEST:
        print('Sunrise: {} Sunset: {} PDT'.
               format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))
    return [today_sr.time(), today_ss.time()]

# Set the backlight to the indicated percent (0-100), over the given fade time.
def fadeTo(brightPercent, durationSeconds):
    backlight = Backlight()
    with backlight.fade(duration=durationSeconds):
        backlight.brightness = brightPercent


if __name__ == "__main__":

    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")

    rise, set = getRiseAndSet(LATITUDE, LONGITUDE)
    if TEST:
        print(f"Rise {rise}, set {set}")
        print(f"Type is {type(rise)}") 

    utc = pytz.UTC
    now = utc.localize(datetime.now()).time()
    print(f"Current time is {now}")

    if TEST:
        print(f"before rise? {now < rise}")
        print(f"after  rise? {now > rise}")
        print(f"before set?  {now < set}")
        print(f"after  set?  {now > set}")

    backlight = BACKLIGHT_NIGHT   
    if now > rise:
        backlight = BACKLIGHT_DAY
    if now > set:
        backlight = BACKLIGHT_NIGHT

    if TEST:
        print(f"backlight: {backlight}")

    
    if TEST:
        print("Test mode - NOT setting")
    else:
        fadeTo(backlight * 100, 5)
        print(f"Set backlight to {backlight} at {now}")

