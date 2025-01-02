import reflex as rx
from reflex_local_auth.pages import login_page
from reflex_local_auth.pages.registration import RegistrationState
from .forms import my_register_form
from ..ui.base import base_page

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