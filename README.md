# home-assistant-tesla
Tesla Motors module for Home Assistant

This is currently just a dirty mqtt script which will be converted to a proper module. Hopefully =)

# Usage
* Clone https://github.com/gglockner/teslajson
* Add your tesla credentials and mqtt credentials to tesla.py
* Run tesla.py

# Warning
The Tesla Motors API isn't official, as far as I know. If you spam them, they will temporarily block API (and app) access to your car. I'm running it 3 times an hour during daytime without getting locked out.

# TODO
* Check how a module should be structured, and implement
* Move authentication and settings out of script
* Find out how dependencies are installed (teslajson)
* Implement switches (current is only sensors)
* Add _all_ sensors
