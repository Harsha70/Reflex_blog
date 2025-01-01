import reflex as rx
from ..ui.base import base_page
from . import forms

from .state import BlogEditPostFormState

# class EditExampleState(rx.State):
#     title: str = "Hello World"
#     content: str = "This is an example blog post."
#     def handle_submit(self, form_data):
#         print(form_data)
#     def handle_content_change(self, value):
#         self.content = value


def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditPostFormState.post
    my_child = rx.vstack(
        rx.heading("Edit ",post.title , size = "9"),
        rx.desktop_only(rx.box(my_form, width = "50vw")),
        rx.mobile_only(rx.box(my_form, width = "95vw")),
        rx.tablet_only(rx.box(my_form, width = "75vw")),
        spacing = "5",
        align = "center",
        min_height ="95vh",
    )
    return base_page(my_child)
