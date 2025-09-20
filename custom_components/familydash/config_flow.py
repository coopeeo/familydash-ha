import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    VERSION = 1

    async def async_step_user(self, info):
        if info is not None:
            return self.async_create_entry(title="FamilyDash", data=info)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("hostname"): str,
                    vol.Required("port", default=8080): int,
                }
            ),
        )

    async def async_step_zeroconf(self, discovery_info):
        """Handle zeroconf discovery."""
        # ZeroconfServiceInfo uses attributes, not dict access
        hostname = getattr(discovery_info, "host", None)
        port = getattr(discovery_info, "port", 8080)

        # Optionally, pre-fill the form with discovered values
        return await self.async_step_user({"hostname": hostname, "port": port})
