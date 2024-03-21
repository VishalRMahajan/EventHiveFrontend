import reflex as rx


def success() -> rx.Component:
    return rx.fragment(
        rx.heading("Payment Successful", size="8", align="center"),
        rx.text("Thank you for your payment!"),
    )