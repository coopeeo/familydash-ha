from .const import DOMAIN


async def async_setup(hass, config):
    hass.states.async_set(f"{DOMAIN}.hello_world", "Hello World!")

    return True
