import reflex as rx


def otp() -> rx.Component:
    rx.popover.content(
        rx.flex(
            rx.text("Simple Example"),
            rx.popover.close(
                rx.button("Close"),
            ),
            direction="column",
            spacing="3",
        ),
    ),