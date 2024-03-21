"""The settings page."""

from EventHive.templates import ThemeState, template
from EventHive.State.eventbookedstate import EventBookedState
import reflex as rx




@template(route="/eventbooked", title="My Event Status (for Committee)", on_load=EventBookedState.login_required)
def eventstatus() -> rx.Component:
   return rx.center(
      rx.data_table(
        data=EventBookedState.booked_tickets,
        columns=EventBookedState.columns,
    )
   )