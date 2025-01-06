"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from rxconfig import config

from .ui.base import base_page
# from pages.about import about_page

from .auth.pages import (my_login_page, my_signup_page, my_logout_page)

from .auth.state import SessionState

from . import  navigations, pages, contact, blog

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    my_user_obj = SessionState.authenticated_user_info
    return base_page(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.text(my_user_obj.to_string()), 
            # rx.text(my_user_obj.user.to_string()), 
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align_items = 'center',
            id='my-child',
        )
    # )
    )
    
app = rx.App()
app.add_page(index)
#

app.add_page(my_login_page,
             route=reflex_local_auth.routes.LOGIN_ROUTE,
             title='Login')

app.add_page(my_signup_page,
             route=reflex_local_auth.routes.REGISTER_ROUTE,
             title='Register')

app.add_page(my_logout_page,
             route=navigations.routes.LOGOUT_ROUTE,
             title='Logout')

app.add_page(pages.about_page, route=navigations.routes.ABOUT_US_ROUTE)
app.add_page(pages.pricing_page, route=navigations.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, route=navigations.routes.CONTACT_US_ROUTE)

app.add_page(pages.protected_page, route='/protected', on_load=SessionState.on_load)

app.add_page(
    contact.contact_entries_list_page, 
    route=navigations.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
    )

app.add_page(
    blog.blog_post_list_page, 
    route=navigations.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.load_posts
    )

app.add_page(
    blog.blog_post_add_page, 
    route=navigations.routes.BLOG_POSTS_ADD_ROUTE,
    )

app.add_page(
    blog.blog_post_detail_page, 
    route='/blog/[blog_id]',
    on_load=blog.BlogPostState.get_post_detail,
    )

app.add_page(
    blog.blog_post_edit_page, 
    route='/blog/[blog_id]/edit',
    on_load=blog.BlogPostState.get_post_detail,
    )