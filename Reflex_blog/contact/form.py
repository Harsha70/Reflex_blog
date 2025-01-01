import reflex as rx
from .state import ContactState

def contact_form() -> rx.Component:
    return rx.form(
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
