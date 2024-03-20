"""The settings page."""

from EventHive.templates import ThemeState, template
from EventHive.State.ProfileState import ProfileState
from EventHive.State.LoginState import LoginFormState
import reflex as rx




@template(route="/profile", title="Profile", on_load=ProfileState.login_required)
def profile() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.heading("Profile", align="center"),
            rx.form.root(
            rx.flex(
                rx.grid(
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=ProfileState.fname,
                                disabled=True,
                                name="fname",
                                size="2",
                            ),
                            as_child=True,
                        ),
                        name="fname",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=ProfileState.lname,
                                disabled=True,
                                size="2",
                            ),
                            as_child=True,
                        ),
                        name="lname",
                    ),
                    columns="2",
                    spacing="1",
                    width="100%",
                ),
                rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=ProfileState.email,
                                disabled=True,
                                name="email",
                                size="2",
                            ),
                            as_child=True,
                        ),
                    name="email",
                    required=True,
                ),
                rx.form.field(
                    rx.form.control(
                        rx.input.input(
                            value=ProfileState.role,
                            disabled=True,
                            size="2",
                        ),
                        as_child=True,
                    ),
                    name="Role",
                ),
                direction="column",
                spacing="4",
                width="18em",
            ),
            reset_on_submit=True,
        ),
            padding="2em",
            class_name="bg-white backdrop-blur-md rounded-lg shadow-lg",
            direction="column",
            spacing="2",
            align="center",
        ),
        width="100%",
        height="100vh",
        bg_color="teal",
    )