"""The dashboard page."""

from EventHive.templates import template

import reflex as rx
from EventHive.State.loginrequired import LoginReqState
from EventHive.State.dashboardstate import DashboardState
from EventHive.State.viewdetails import viewdetailsState

def render_event(event: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(event['event_name'], align="center"),
            rx.flex(
                rx.text(f"Venue: {event['venue']}"),
                rx.text(f"Date: {event['date']}"),
                rx.text(f"Time: {event['time']}"),
                rx.text(f"Price: {event['ticket_price']}"),
                direction="row",
                spacing="2",
            ),
            rx.scroll_area(
                rx.text(event['description'],class_name="text-justify"),
                max_height="200px"
            ),
            rx.grid(
                rx.button("View Details", on_click=viewdetailsState.onclick(event["event_name"])),
                rx.button("Buy Ticket", on_click=viewdetailsState.payment(event["ticket_price"])),
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
        rx.foreach(DashboardState.events, render_event),
        columns=[1, 2, 3],
        spacing="4",
        class_name="mt-4",
    )

@template(route="/dashboard", title="Dashboard", on_load=DashboardState.login_required)
def dashboard() -> rx.Component:
    return rx.fragment(
        rx.heading("Dashboard", size="8", align="center"),
        card_render(),
    )
