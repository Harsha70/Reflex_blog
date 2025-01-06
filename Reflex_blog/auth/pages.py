import reflex as rx
from reflex_local_auth.pages import login_page
from reflex_local_auth.pages.registration import RegistrationState
from .forms import my_register_form
from ..ui.base import base_page
from .. import navigations
from .state import SessionState


def my_login_page()->rx.Component:
    return base_page(login_page())


def my_signup_page()->rx.Component:
    return base_page(
        rx.center(
            rx.cond(
            RegistrationState.success,
            rx.vstack(
                rx.text("Registration successful!"),
            ),
            rx.card(my_register_form()),
        ),
            padding = '4em'
        )
    )


def my_logout_page() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        # rx.container(
        
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Are you sure you want to logout?", size="9"),
            rx.hstack(
                rx.button(
                    "Yes", 
                    on_click=SessionState.perform_logout,
                    color_scheme="red"
                ),
                rx.link(
                    rx.button("No", color_scheme="gray"),
                    href=navigations.routes.HOME_ROUTE
                ),
                spacing="3",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align_items="center",
            id="my-child",
        )
    # )
    )