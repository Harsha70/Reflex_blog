import reflex as rx
from .state import ContactState
from ..auth.state import SessionState

def contact_form() -> rx.Component:
    user_id = SessionState.my_user_id
    return rx.form(
        rx.cond(user_id,
                rx.box(
                    rx.input(
                        type="hidden",
                        name="user_id",
                        value=user_id,
                    ), display="none"),
                    rx.fragment(""),
        ),
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        type="text",
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.input(
                    type="email",
                    name="email",
                    width="100%",
                    plactholder = "Email Address"
                ),
                rx.text_area(
                    name='message', 
                    placeholder="Message",
                    required=True,
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        )
