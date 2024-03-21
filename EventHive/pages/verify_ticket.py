import reflex as rx
from EventHive.State.VerifyTicketState import VerifyTicket

def verify_ticket() -> rx.Component:
    return rx.vstack(
        rx.text(f"Event Name: {VerifyTicket.event_name}"),
        rx.text(f"Email: {VerifyTicket.email1}"),
        rx.text(f"Committee: {VerifyTicket.committee}"),
        rx.text(f"Is the ticket valid?: {VerifyTicket.valid}"),
    )
