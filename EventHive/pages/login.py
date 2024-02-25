from rxconfig import config
from typing import List
import reflex as rx
import re



class LoginFormState(rx.State):
    # These track the user input real time for validation
    user_entered_email: str
    user_entered_password: str

    # These are the submitted data
    usertype: str
    email: str
    password: str
    form_data: dict = {}
    
    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(
            r"[^@]+@(student\.sfit\.ac\.in|sfit\.ac\.in)$", self.user_entered_email
        )

    @rx.var
    def invalid_password(self) -> bool:
        return len(self.user_entered_password) < 8

    @rx.var
    def input_invalid(self) -> bool:
        return (
            self.invalid_email
            or self.invalid_password
        )

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.usertype = form_data.get("usertype")
        self.email = form_data.get("email")
        self.password = form_data.get("password")
        print(self.usertype, self.email, self.password)
        print(form_data)

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