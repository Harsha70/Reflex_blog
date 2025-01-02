import reflex as rx
import reflex_local_auth
from .. import navigations



def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", navigations.routes.ABOUT_US_ROUTE),
                    navbar_link("Blog", navigations.routes.BLOG_POSTS_ROUTE),
                    navbar_link("Pricing", navigations.routes.PRICING_ROUTE),
                    navbar_link("Contact", navigations.routes.CONTACT_US_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Sign Up",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE,
                    ),
                    rx.link(
                        rx.button(
                            "Login",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE,
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigations.NavState.to_home),
                        rx.menu.item("About", on_click=navigations.NavState.to_about_us),
                        rx.menu.item("Blog", on_click=navigations.NavState.to_blog),
                        rx.menu.item("Pricing", on_click=navigations.NavState.to_pricing),
                        rx.menu.item("Contact", on_click=navigations.NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=navigations.NavState.to_login),
                        rx.menu.item("Sign up", on_click=navigations.NavState.to_signup),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )