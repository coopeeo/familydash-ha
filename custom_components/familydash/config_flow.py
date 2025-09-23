import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class FamilyDashConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """FamilyDash config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, any] | None = None,  # type: ignore  # noqa: PGH003
    ) -> config_entries.ConfigFlowResult:
        if user_input is not None:
            return await self.async_step_link(user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("IP Address"): str,
                }
            ),
        )

    async def async_step_link(
        self,
        user_input: dict[str, any] | None = None,  # type: ignore  # noqa: PGH003
    ) -> config_entries.ConfigFlowResult:
        if user_input is None:
            return self.async_show_form(step_id="link")

        return self.async_show_progress(step_id="link", progress_action="Loading")
