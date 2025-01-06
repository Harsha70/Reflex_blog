import reflex as rx 
# from .nav import navbar
from .sidebar import sidebar
def base_dashboard_page(child: rx.Component, *args, **kwargs)->rx.Component:
    return rx.fragment(
        rx.hstack(
        sidebar(),
        rx.box(child, 
               rx.logo(), 
               padding = '1em',
               width = '100%',
               id = 'my_box_base_container'),
        ),
        rx.color_mode.button(position="bottom-right"),
        # id = 'my_base_container'
    )
    