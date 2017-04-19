import logging
from datetime import timedelta
#from homeassistant.util import Throttle
from homeassistant.const import STATE_UNKNOWN, TEMP_CELSIUS
#import teslajson We can't excpet everyone to manually install this module so we should make our own implementation? I took a look at the Tesla documentation and it doesn't seem too hard to implement.

_LOGGER = logging.getLogger(__name__)

# The domain of your component. Should be equal to the name of your component.
DOMAIN = 'tesla'
DEPENDENCIES = []

CONF_INTERVAL = 'interval'
DEFAULT_INTERVAL = timedelta(hours=12) #TODO: Implement better timing system. Maybe no updates during night but more during day?
                                       #      Maybe take some inspiration from https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/weather/openweathermap.py
                                       #      For more details see update()
CONF_USERNAME = 'username'
CONF_PASSWORD = 'password'
CONF_NAME = 'name'

DEFAULT_NAME = 'Tesla Vehicle'
ATTRIBUTION = 'Data provided by Tesla, Inc.'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_INTERVAL, default=DEFAULT_INTERVAL): cv.int,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
})

class TeslaVehicle():
    """"Implementation of a Tesla electric vehicle"""
    def __init__(self, hass, config):
        _LOGGER.info("Running setup.")

        # Get data from the configuration.
        self.hass = hass
        self._name = config[DOMAIN].get(CONF_NAME) #TODO: Get vehicle name?
        self._interval = config[DOMAIN].get(CONF_INTERVAL)
        self.data = None # This will later on store vehicle data
        username = config[DOMAIN].get(CONF_USERNAME)
        password = config[DOMAIN].get(CONF_PASSWORD)

        # States are in the format DOMAIN.OBJECT_ID
        hass.states.set(DOMAIN + '.User_State', username)

        #TODO: Run authentication. What's the timeout for connections to tesla service?
        #      We probably have to reauthenticate at a later point so put authentication in it's own function.
        if username and password:
            self.authenticate()
        
        # Return boolean to indicate that initialization was successfully.
        _LOGGER.info("Setup successful.")
        return True

    def authenticate(self):
        """"Authenticate at tesla service with given username and password"""
        #self._auth = Some sort of token or cookie?
        pass

    #@Throttle(DEFAULT_INTERVAL) # Maybe use this timing system? If yes uncomment 'from homeassistant.util import Throttle' in one of the first lines
    def update(self):
        """Get updated data from the vehicle"""
        #TODO: Maybe add a class to contain vehicle data?
        pass
    
    @property
    def name(self):
        """Return the name of this device."""
        return self._name
