from .const import DOMAIN

async def async_setup(hass, config):
    """Set up this component using YAML is not supported."""
    hass.states.async_set(f"{DOMAIN}.hello_world", "Hello World!")

    return True