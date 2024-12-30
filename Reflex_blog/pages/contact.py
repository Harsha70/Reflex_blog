import reflex as rx

from .. import navigations
from ..ui.base import base_page

class ContactState(rx.State):
    form_data: dict = {}
    
    print(form_data)
    def handle_submit(self, form_data: dict):
        self.form_data = form_data

@rx.page(route=navigations.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
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
    my_child = rx.vstack(
        rx.heading("Contact Us", size = "9"),
        rx.cond(True, "Submitted", "Default"),
        rx.desktop_only(rx.box(my_form, width = "50vw")),
        rx.mobile_only(rx.box(my_form, width = "95vw")),
        rx.tablet_only(rx.box(my_form, width = "75vw")),
        spacing = "5",
        justify = "center",
        align = "center",
        min_height ="85vh",
        id = "my_child"
    )
    return base_page(my_child)