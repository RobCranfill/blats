# blats - Back Light According To Sun 
A Python applet to set the backlight of the RPi's LCD according to the time of day.
To be run with cron. 

This is somewhat obsoleted by my "blatb" project, which uses an ambient light sensor.

Example cron entry:
``` 
    0 * * * * /home/pi/proj/blats/blats.sh
``` 


Requires:
* Raspberry Pi with 7-inch LCD touchscreen version 1.1 or newer
* https://rpi-backlight.readthedocs.io/en/latest/ (pip3 install rpi_backlight)
* https://github.com/SatAgro/suntime (pip3 install suntime)
* https://pypi.org/project/pytz/ (pip3 install pytz)
* You must also either run this as root (not recommended), or set the permissions for the device (pseudo-)files as shown in the included "udev" rules.

