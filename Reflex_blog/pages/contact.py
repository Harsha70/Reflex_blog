# import reflex as rx

# from .. import navigations
# from ..ui.base import base_page

# from .. import contact

# @rx.page(route=navigations.routes.CONTACT_US_ROUTE)
# def contact_page() -> rx.Component:
#     my_form = contact.contact_form
#     my_child = rx.vstack(
#         rx.heading("Contact Us", size = "9"),
#         rx.cond(contact.ContactState.did_submit, contact.ContactState.thank_you, ""),
#         rx.desktop_only(rx.box(my_form, width = "50vw")),
#         rx.mobile_only(rx.box(my_form, width = "95vw")),
#         rx.tablet_only(rx.box(my_form, width = "75vw")),
#         spacing = "5",
#         justify = "center",
#         align = "center",
#         min_height ="85vh",
#         id = "my_child"
#     )
#     return base_page(my_child)