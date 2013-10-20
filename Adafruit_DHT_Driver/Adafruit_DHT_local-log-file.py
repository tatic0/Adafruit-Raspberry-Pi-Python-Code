#!/usr/bin/python

## This script is based on the examples provided by Adafruit.
## See README for Copyright information

import subprocess
import re
import sys
import time


try:
# Continuously append data
  while(True):
    # Run the DHT program to get the humidity and temperature readings!
    # open log file to write
    logfile=open('temp-hum.log','a')

    output = subprocess.check_output(["./Adafruit_DHT", "22", "4"]);
    print output
    # search for temperature printout
    matches = re.search("Temp =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    temp = float(matches.group(1))
    
    # search for humidity printout
    matches = re.search("Hum =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    humidity = float(matches.group(1))
    
    now = time.time()
    data =("%s %.1f %.1f\n") % (now,temp,humidity)
    print(data)
    logfile.write(data)
    logfile.close()
    # Wait half an hour between each measurement
    time.sleep(1800)
except KeyboardInterrupt:
  print("You pressed ctrl-c, quitting")
  logfile.close()
  sys.exit(0)
