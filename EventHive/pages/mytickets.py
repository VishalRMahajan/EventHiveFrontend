"""The dashboard page."""

from EventHive.templates import template

import reflex as rx
from EventHive.State.loginrequired import LoginReqState
from EventHive.State.dashboardstate import DashboardState
from EventHive.State.viewdetails import viewdetailsState
from EventHive.State.myticketsstate import MyTicketState

def render_event(tickets: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(tickets['event_name'], align="center"),
            rx.image(src=tickets['qr_url'], alt="Event Image", width="200px", height="200px", align="center"),
            rx.grid(
                rx.button("More Details", on_click=viewdetailsState.onclick(tickets["event_name"])),
                rx.button("Download QR", on_click=rx.download(url=tickets["qr_url"],)),
                columns="2",
                spacing="2",
                align="center",
            ),
            spacing="3",
            align="center"
        ),
        style={"maxWidth": "500px"}
    )

def card_render() ->rx.Component:
    return rx.chakra.responsive_grid(
        rx.foreach(MyTicketState.tickets, render_event),
        columns=[1, 2, 3],
        spacing="4",
        class_name="mt-4",
    )

@template(route="/mytickets", title="My Tickets", on_load=MyTicketState.login_required)
def mytickets() -> rx.Component:
    return rx.fragment(
        rx.heading("My Tickets", size="8", align="center"),
        rx.cond(
                viewdetailsState.error,
                rx.callout(
                    viewdetailsState.error_text,
                    icon="alert_triangle",
                    color_scheme="red",
                    role="alert",
                    width="100%",
                    size="1",
                    align="center",
                ),
            None,
        ),
        card_render(),
    )
