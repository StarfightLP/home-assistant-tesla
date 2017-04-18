# home-assistant-tesla
Tesla Motors module for Home Assistant

This is currently just a dirty mqtt script which will be converted to a proper module. Hopefully =) Borne from discussion at https://community.home-assistant.io/t/tesla-motors-api-support-for-tracking/4782/6

# Usage
* Clone https://github.com/gglockner/teslajson
* Add your tesla credentials and mqtt credentials to tesla.py
* Run tesla.py

# Configuration in Home Assistant
  
  - platform: mqtt
    state_topic: "sensor/tesla/battery_level"
    name: Tesla battery level
    unit_of_measurement: '%'
    expire_after: 1800
  - platform: mqtt
    state_topic: "sensor/tesla/inside_temp"
    name: Tesla inside temp
    unit_of_measurement: '°C'
    expire_after: 1800
  - platform: mqtt
    state_topic: "sensor/tesla/outside_temp"
    name: Tesla outside temp
    unit_of_measurement: '°C'
    expire_after: 1800
  - platform: mqtt
    state_topic: "sensor/tesla/speed"
    name: Speed
    unit_of_measurement: 'kmh'
    expire_after: 1800
  - platform: mqtt
    state_topic: "sensor/tesla/battery_current"
    name: Battery current
    unit_of_measurement: 'A'
    expire_after: 1800
  - platform: mqtt
    state_topic: "sensor/tesla/charging_state"
    name: Charging state
    expire_after: 1800


# Warning
The Tesla Motors API isn't official, as far as I know. If you spam them, they will temporarily block API (and app) access to your car. I'm running it 3 times an hour during daytime without getting locked out.

# TODO
* Check how a module should be structured, and implement
* Move authentication and settings out of script
* Find out how dependencies are installed (teslajson)
* Implement switches (current is only sensors)
* Add _all_ sensors
