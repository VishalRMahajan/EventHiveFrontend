"""Welcome to Reflex!."""

from EventHive import styles
from EventHive.State.loginrequired import LoginReqState
# Import all the pages.
from EventHive.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)
app.add_page(login, "/", title="Login", on_load=LoginReqState.already_logged_in)
app.add_page(register, "/register", title="Register", on_load=LoginReqState.already_logged_in)
