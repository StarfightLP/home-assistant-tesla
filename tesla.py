#!/usr/bin/env python3 

# Tesla API docs:
#http://docs.timdorr.apiary.io/#reference/vehicles/state-and-settings/climate-settings

import teslajson
import subprocess 

c = teslajson.Connection('me@example.com', 'password') 
v = c.vehicles[0]
verbose=False 

#v.wake_up() # May be needed to get all data, but will also increase car battery usage

charge_state=v.data_request('charge_state') 

for key, value in charge_state.items(): 
  if verbose:
    print("*", key, "->", value) 

  subprocess.run([ 
    "mosquitto_pub",
    "-h", 
    "192.168.1.11",
    "-u", 
    "tesla",
    "-P",
    "password",
    "-t",
    "sensor/tesla/" + key,
    "-r",
    "-m",
    str(value)
])

climate_state = v.data_request('climate_state') 

for key, value in climate_state.items():
  if verbose:
    print("*", key, "->", value)

  subprocess.run([
    "mosquitto_pub",
    "-h",
    "192.168.1.11",
    "-u",
    "tesla",
    "-P",
    "password",
    "-t",
    "sensor/tesla/" + key,
    "-r",
    "-m",
    str(value)
])

drive_state = v.data_request('drive_state')

for key, value in drive_state.items():
  if verbose:
    print("*", key, "->", value)

  subprocess.run([
    "mosquitto_pub",
    "-h",
    "192.168.1.11",
    "-u",
    "tesla",
    "-P",
    "password",
    "-t",
    "sensor/tesla/" + key,
    "-r",
    "-m",
    str(value)
])

# fake owntracks
speed = drive_state['speed']
lat = drive_state['latitude']
lon = drive_state['longitude']
tst = drive_state['gps_as_of']
subprocess.run([
  "mosquitto_pub",
  "-h",
  "192.168.1.11",
  "-u",
  "tesla",
  "-P",
  "password",
  "-t",
  "owntracks/sensor/tesla",
  "-r",
  "-m",
  '{"_type":"location","tid":"T","acc":10,"batt":' + str(charge_state['battery_level']) + ',"conn":"m","doze":false,"lat":' + str(lat) + ',"lon":' + str(lon) + ',"tst":' + str(tst) + '}'
])

# Example of a proper owntracks run:
# owntracks/lars/fp2 {"_type":"location","tid":"L","acc":9,"batt":91,"conn":"m","doze":false,"lat":59.123293,"lon":10.123602,"tst":1488789605}

