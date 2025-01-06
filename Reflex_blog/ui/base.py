import reflex as rx 

from ..auth.state import SessionState
from .nav import navbar
from .dashboard import base_dashboard_page

def base_layout_component(child: rx.Component, *args, **kwargs)->rx.Component:
    return rx.fragment(
        
        navbar(),
        rx.box(child, id = 'my_box_base_container'),
        rx.logo(),
        rx.color_mode.button(position="top-right"),
        # id = 'my_base_container'
    )

def base_page(child: rx.Component, *args, **kwargs)->rx.Component:
    # is_logged_in = True
    
    return rx.cond(SessionState.is_authenticated, base_dashboard_page(child, *args, **kwargs), 
                   base_layout_component(child, *args, **kwargs)
                   )