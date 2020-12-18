#!/bin/bash
export PYTHONPATH=/home/pi/.local/bin:/home/pi/.local/lib:/home/pi/.local/share
echo Pythonpath is $PYTHONPATH

python3 /home/pi/proj/blats/blats.py >>/home/pi/proj/blats/blats.log

