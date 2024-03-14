"""Sidebar component for the app."""

from EventHive import styles
from EventHive.State.loginrequired import LoginReqState
import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.spacer(),
        rx.color_mode_cond(
            rx.image(src="/Eventhive.png", height="3em"),
            rx.image(src="/Eventhive.png", height="3em"),
        ),
        rx.spacer(),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding="2em 1em 1em 1em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.button(
            "Logout",
            on_click=LoginReqState.logout,
        ),
        rx.spacer(),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == f"/{text.lower()}") | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.center(
                rx.image(
                    height="2.5em",
                    padding="0.5em",
                ),
                rx.text(
                    text,
                    align="center",
                ),
                bg=rx.cond(
                    active,
                    styles.accent_color,
                    "transparent",
                ),
                color=rx.cond(
                    active,
                    styles.accent_text_color,
                    styles.text_color,
                ),
            ),
            align="center",
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        icon=page.get("image", "/github.svg"),
                        url=page["route"],
                    )
                    for page in get_decorated_pages()
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
