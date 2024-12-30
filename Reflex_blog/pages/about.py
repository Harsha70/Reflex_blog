import reflex as rx

from ..ui.base import base_page

def about_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("About Us", size = "9"),
        rx.text("something cool"),
        spacing = "5",
        justify = "center",
        align = "center",
        min_height ="85vh",
        id = "my_child"
    )
    return base_page(my_child)

