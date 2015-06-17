#!/usr/bin/python

## This script is based on the examples provided by Adafruit.
## See README for Copyright information

import subprocess
import re
import sys
import time
import sqlite3

try:
# Continuously append data
  while True:
    #logfile=open('temp-hum.log','a')
    conn = sqlite3.connect("thg.db")
    # Run the DHT program to get the humidity and temperature readings!
    #output = subprocess.check_output(["./Adafruit_DHT", "22", "4"]);
    output = subprocess.check_output(["./Adafruit_DHT", "22", "4"]); ### DEBUG
    print output
    # search for temperature printout
    matches = re.search("Temp =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    temp = str(float(matches.group(1)))
    
    # search for humidity printout
    matches = re.search("Hum =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    humidity = str(float(matches.group(1)))
    
    now = str(time.time())
    print(now,temp,humidity)
    curs = conn.cursor()
    curs.execute("INSERT INTO sensordata ('date','temp','humidity') VALUES (?,?,?)", (now, temp, humidity))
    conn.commit()
    # Wait half an hour between each measurement
    time.sleep(18) # DEBUG
    #time.sleep(1800)
except KeyboardInterrupt:
  print("You pressed ctrl-c, quitting")
  conn.close()
  sys.exit(0)
