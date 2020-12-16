# blats - Back Light According To Sun 
A Python applet to set the backlight of the RPi's LCD according to the time of day.
To be run with cron.

Example cron entry:
``` 
    0 * * * * /home/pi/proj/blats/blats.sh
``` 

Requires:
* Raspberry Pi with 7-inch LCD touchscreen version 1.1 or newer
* https://rpi-backlight.readthedocs.io/en/latest/index.html#
* https://github.com/SatAgro/suntime
* You must also either run this as root (not recommended), or set the permissions for the device (pseudo-)files as shown in the included "udev" rules.

