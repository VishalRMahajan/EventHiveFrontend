"""The dashboard page."""

from EventHive.templates import template

import reflex as rx
from EventHive.State.loginrequired import LoginReqState

@template(route="/dashboard", title="Dashboard", on_load=LoginReqState.login_required)
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.flex(
        rx.heading("Dashboard", size="8", align="center"),
        rx.text("Welcome to EventHive!", align="center"),
        direction="column", 
    )
