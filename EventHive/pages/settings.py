"""The settings page."""

from EventHive.templates import ThemeState, template

import reflex as rx


@template(route="/settings", title="Settings")
def settings() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Settings", size="8"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/settings.py"),
            size="1",
        ),
    )
