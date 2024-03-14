from rxconfig import config
import reflex as rx
from ..State.RegisterState import RegisterFormState




def register() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.heading("Register", align="center"),
            rx.text("Fill the Following Details",),
            rx.cond(
                RegisterFormState.error,
                rx.callout(
                    RegisterFormState.error_text,
                    icon="alert_triangle",
                    color_scheme="red",
                    role="alert",
                    width="20em",
                    size="1",
                ),
                None,
            ),
            rx.form.root(
            rx.flex(
                rx.select.root(
                    rx.select.trigger(placeholder="Register As"),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item("Student", value="student"),
                            rx.select.item("Committee", value="committee"),
                            name="usertype",
                            required=True,
                        ),
                        color_scheme="teal",
                    ),
                    name="usertype",
                ),
                rx.grid(
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                placeholder="First Name",
                                name="fname",
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="fname",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Last Name",
                                name="lname",
                                size="2",
                                required=True,
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
                                placeholder="Email Address",
                                on_change=RegisterFormState.set_user_entered_email,
                                name="email",
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "Enter email address with domain @student.sfit.ac.in",
                            match="valueMissing",
                            force_match=RegisterFormState.invalid_email,
                            color="var(--red-11)",
                            font_size="0.85em",
                        ),
                    name="email",
                    server_invalid=RegisterFormState.invalid_email,
                ),
                rx.form.field(
                    rx.form.control(
                        rx.input.input(
                            placeholder="Password",
                            on_change=RegisterFormState.set_user_entered_password,
                            name="password",
                            type="password",
                            size="2",
                            min_length=8,
                            required=True,
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Password should be at least 8 characters long",
                        match="tooShort",
                        force_match=RegisterFormState.invalid_password,
                        color="var(--red-11)",
                        font_size="0.85em",
                    ),
                    name="password",
                ),
                rx.form.submit(
                    rx.button(
                        "Submit",
                        disabled=RegisterFormState.input_invalid,
                        color_scheme="teal",
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="20em",
            ),
            on_submit=RegisterFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.text(
            "Already Registered? ",
             rx.link(
                rx.button("Login", color_scheme="teal"),
                href="/",
                color_scheme="teal",
                button=True,
                ),
             padding="0.5em 0 0 0",
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