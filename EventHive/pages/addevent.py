"""The settings page."""

from EventHive.templates import ThemeState, template
from EventHive.State.AddeventState import Addevent
from EventHive.State.RegisterState import RegisterFormState
import reflex as rx




@template(route="/addevent", title="Add Event", on_load=Addevent.login_required)
def addevent() -> rx.Component:
   return rx.center(
        rx.flex(
            rx.heading("Add Event", align="center"),
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
               rx.grid(
                    rx.select.root(
                        rx.select.trigger(placeholder="Committe Name"),
                        rx.select.content(
                            rx.select.group(
                                rx.select.item("ITSA", value="ITSA"),
                                rx.select.item("CSI", value="CSI"),
                                rx.select.item("ISTE", value="ISTE"),
                                rx.select.item("IEEE", value="IEEE"),
                                rx.select.item("MESA", value="MESA"),
                                rx.select.item("SFITAA", value="SFITAA"),
                                rx.select.item("Student Council", value="Student Council"),
                                name="committee_name",
                                required=True,
                            ),
                            color_scheme="teal",
                        ),
                        name="committee_name",
                    ),
                    rx.form.field(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Event Name",
                                name="event_name",
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
                                placeholder="Venue",
                                name="venue",
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
                                placeholder="Date",
                                name="Date",
                                type="date",
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
                                placeholder="Time",
                                name="Time",
                                type="time",
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
                                placeholder="Ticket Price",
                                name="Date",
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
                                placeholder="Contact Person",
                                name="contact_person",
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
                                placeholder="Contact Number",
                                type="text",
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
                    placeholder="Description",
                    name="description",
                    height="10em",
                ),
                rx.form.submit(
                    rx.button(
                        "Submit",
                        color_scheme="teal",
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="40em",
            ),
            on_submit=RegisterFormState.handle_submit,
            reset_on_submit=True,
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