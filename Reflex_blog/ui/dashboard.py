import reflex as rx 
# from .nav import navbar
from .sidebar import sidebar
def base_dashboard_page(child: rx.Component, *args, **kwargs)->rx.Component:
    return rx.fragment(
        sidebar(),
        rx.box(child, id = 'my_box_base_container'),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id = 'my_base_container'
    )
    