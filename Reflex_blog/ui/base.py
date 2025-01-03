import reflex as rx 
from .nav import navbar
from .dashboard import base_dashboard_page

def base_page(child: rx.Component, *args, **kwargs)->rx.Component:
    is_logged_in = True
    
    return rx.fragment(
        navbar(),
        rx.box(child, id = 'my_box_base_container'),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id = 'my_base_container'
    )
    