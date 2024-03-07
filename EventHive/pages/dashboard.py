"""The dashboard page."""
import requests
from EventHive.templates import template
from EventHive.State.loginrequired import LoginReqState 
import reflex as rx

class DashboardState(rx.State):
    pass

@template(route="/dashboard", title="Dashboard", on_load=LoginReqState.login_required)
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.chakra.vstack(
        rx.chakra.heading("Dashboard", font_size="3em"),
        rx.chakra.text("Welcome to Reflex!"),
        rx.chakra.text(
            "You can edit this page in ",
            rx.chakra.code("{your_app}/pages/dashboard.py"),
        ),
    )
