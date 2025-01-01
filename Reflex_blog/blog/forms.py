import reflex as rx
from .state import (BlogEditPostFormState, BlogAddPostFormState)

def blog_post_add_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="title",
                        name="title",
                        required=True,
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.text_area(
                    name='content', 
                    placeholder="Message",
                    required=True,
                    width="100%",
                    height = '50vh',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=BlogAddPostFormState.handle_submit,
            reset_on_submit=True,
        )


def blog_post_edit_form() -> rx.Component:
    post = BlogEditPostFormState.post
    title = post.title
    post_content = BlogEditPostFormState.post_content
    return rx.form(
        rx.box(
        rx.input(
            type='hidden',
            name='post_id',
            value=post.id,
            ),
        display = 'none',
        ),
            rx.vstack(
                rx.hstack(
                    rx.input(
                        default_value = title,
                        # on_change = BlogEditPostFormState.set_title,
                        placeholder="title",
                        name="title",
                        required=True,
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.text_area(
                    value = post_content,
                    # on_change = EditExampleState.handle_content_change,
                    on_change = BlogEditPostFormState.set_post_content,
                    name='content', 
                    placeholder="Message",
                    required=True,
                    width="100%",
                    height = '50vh',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=BlogEditPostFormState.handle_submit,
            reset_on_submit=True,
        )
