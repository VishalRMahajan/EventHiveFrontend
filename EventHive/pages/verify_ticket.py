import reflex as rx
from EventHive.State.VerifyTicketState import VerifyTicket

def verify_ticket() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.heading("Ticket Status", align="center"),
            rx.form.root(
            rx.flex(
                rx.text(f"Event Name: {VerifyTicket.event_name}"),
                rx.text(f"Email: {VerifyTicket.email1}"),
                rx.text(f"Organizing Committee: {VerifyTicket.committee}"),
                rx.text(f"Is the Ticket Valid: {VerifyTicket.valid}"),
                rx.cond(
                    VerifyTicket.valid,
                    rx.image(src="/greentick.png", width="100px", height="auto",align="center"),
                    rx.image(src="/redcross.png",  width="100px", height="auto",align="center"),
                ),
                direction="column",
                spacing="4",
                width="15em",
                align="center",
            ),
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
