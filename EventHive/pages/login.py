from rxconfig import config
import reflex as rx
from ..State.LoginState import LoginFormState



def login() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.heading("Login", align="center"),
            rx.text("If you are already a member, easily log in",),
            rx.form.root(
            rx.flex(
                rx.select.root(
                    rx.select.trigger(placeholder="Login As"),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item("Student", value="student"),
                            rx.select.item("Coordinator", value="Coordinator"),
                            name="usertype",
                        ),
                    ),
                    name="usertype",
                    required=True,
                ),
                rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Email Address",
                                on_change=LoginFormState.set_user_entered_email,
                                name="email",
                                size="2",
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "Enter email address with domain @student.sfit.ac.in",
                            match="valueMissing",
                            force_match=LoginFormState.invalid_email,
                            color="var(--red-11)",
                            font_size="0.85em",
                        ),
                    name="email",
                    server_invalid=LoginFormState.invalid_email,
                    required=True,
                ),
                rx.form.field(
                    rx.form.control(
                        rx.input.input(
                            placeholder="Password",
                            on_change=LoginFormState.set_user_entered_password,
                            name="password",
                            type="password",
                            size="2",
                            min_length=8,
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Password should be at least 8 characters long",
                        match="tooShort",
                        force_match=LoginFormState.invalid_password,
                        color="var(--red-11)",
                        font_size="0.85em",
                    ),
                    name="password",
                    required=True,
                ),
                rx.form.submit(
                    rx.button(
                        "Submit",
                        disabled=LoginFormState.input_invalid,
                        color_scheme="teal",
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="20em",
            ),
            on_submit=LoginFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.cond(
            LoginFormState.error,
            rx.text(LoginFormState.error_text, color="var(--red-11)"),
            None,
        ),
        rx.divider(),
        rx.text(
            "Don't have an account yet? ",
             rx.link(
                rx.button("Register", color_scheme="teal"),
                href="/register",
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
        bg_color="#0a192f",
    )