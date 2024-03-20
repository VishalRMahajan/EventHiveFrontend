"""Welcome to Reflex!."""

from EventHive import styles
from EventHive.State.loginrequired import LoginReqState
from EventHive.State.viewdetails import viewdetailsState
# Import all the pages.
from EventHive.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)
app.add_page(login, "/", title="Login", on_load=LoginReqState.already_logged_in)
app.add_page(register, "/register", title="Register", on_load=LoginReqState.already_logged_in)
app.add_page(viewdetails, "/viewdetails", title="Event Details", on_load=viewdetailsState.login_required)
