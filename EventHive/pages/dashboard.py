"""The dashboard page."""
from EventHive.templates import template

import reflex as rx

class DashboardState(rx.State):
    access_token = rx.LocalStorage(name="access_token")

@template(route="/dashboard", title="Dashboard")
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
