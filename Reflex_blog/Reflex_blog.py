"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from rxconfig import config

from .ui.base import base_page
# from pages.about import about_page
from . import auth, navigations, pages, contact, blog

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        # rx.container(
        
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
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

app.add_page(auth.pages.my_login_page,
             route=reflex_local_auth.routes.LOGIN_ROUTE,
             title='Login')

app.add_page(auth.pages.my_signup_page,
             route=reflex_local_auth.routes.REGISTER_ROUTE,
             title='Register')

# app.add_page(reflex_local_auth.pages.register_page,
#              route=reflex_local_auth.routes.REGISTER_ROUTE,
#              title='Register')

app.add_page(pages.about_page, route=navigations.routes.ABOUT_US_ROUTE)
app.add_page(pages.pricing_page, route=navigations.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, route=navigations.routes.CONTACT_US_ROUTE)

app.add_page(pages.protected_page, route='/protected', on_load=auth.SessionState.on_load)

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