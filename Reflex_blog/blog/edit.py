import reflex as rx
from ..ui.base import base_page

class EditExampleState(rx.State):
    title: str = "Hello World"
    content: str = "This is an example blog post."
    def handle_submit(self, form_data):
        print(form_data)
    def handle_content_change(self, value):
        self.content = value

def blog_post_edit_sample_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        default_value = EditExampleState.title,
                        
                        placeholder="title",
                        name="title",
                        required=True,
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.text_area(
                    value = EditExampleState.content,
                    # on_change = EditExampleState.handle_content_change,
                    on_change = EditExampleState.set_content,
                    name='content', 
                    placeholder="Message",
                    required=True,
                    width="100%",
                    height = '50vh',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=EditExampleState.handle_submit,
            reset_on_submit=True,
        )

def blog_post_edit_page() -> rx.Component:
    my_form = blog_post_edit_sample_form()
    my_child = rx.vstack(
        rx.heading("Edit Blog Post", size = "9"),
        rx.desktop_only(rx.box(my_form, width = "50vw")),
        rx.mobile_only(rx.box(my_form, width = "95vw")),
        rx.tablet_only(rx.box(my_form, width = "75vw")),
        spacing = "5",
        align = "center",
        min_height ="95vh",
    )
    return base_page(my_child)
