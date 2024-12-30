import reflex as rx
from .nav import navbar
def base_page(child: rx.Component, *args, **kwargs)->rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(child, id = 'my_box_base_container'),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id = 'my_base_container'
    )
    