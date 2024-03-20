import reflex as rx
from EventHive.templates import template
from EventHive.State.viewdetails import viewdetailsState

def viewdetails() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.heading("EVENTHIVE", align="center"),
            rx.text("Following are the Details of Selected Event",),
            rx.form.root(
            rx.flex(
               rx.grid(
                   rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.committee,
                                disabled=True,
                                name="committee",
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="committee",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.event_name,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="event_name",
                    ),
                    columns="2",
                    spacing="1",
                    width="100%",
               ),
                rx.grid(
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.venue,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="venue",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.date,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="Date",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.time,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="time",
                    ),
                    columns="3",
                    spacing="1",
                    width="100%",
                ),
                rx.grid(
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.ticket_price,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="Ticket_price",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.contact_person,
                                disabled=True,
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="contact_person",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                value=viewdetailsState.contact_number,
                                disabled=True,
                                name="phone",
                                size="2",
                                required=True,
                            ),
                            as_child=True,
                        ),
                        name="phone",
                    ),
                    columns="3",
                    spacing="1",
                    width="100%",
                ),
                rx.text_area(
                    value=viewdetailsState.description,
                    disabled=True,
                    name="description",
                    height="10em",
                ),
                rx.button(
                    "Buy Ticket",
                    color_scheme="teal",
                ),
                direction="column",
                spacing="4",
                width="40em",
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
