import reflex as rx

from ..ui.base import base_page

from . import state

def blog_post_detail_page() -> rx.Component:
    can_edit=True
    edit_links=rx.link('Edit', href=f'/blog/{state.BlogPostState.blog_post_id}/edit')
    edit_link_el = rx.cond(
        can_edit,
        edit_links,
        rx.fragment(''),
    )
    my_child = rx.vstack(
        rx.heading(state.BlogPostState.post.title, size = "9"),
        rx.text("user info id: ",state.BlogPostState.post.userinfo_id),
        rx.text("post :",state.BlogPostState.post.to_string()),
        rx.text("user info: ",state.BlogPostState.post.userinfo.to_string()),
        rx.text("user: ",state.BlogPostState.post.userinfo.user.to_string()),
        rx.text(state.BlogPostState.post.publish_date),
        edit_link_el,
        # rx.text(state.BlogPostState.blog_post_id),
        rx.text(state.BlogPostState.post.content, white_space='pre-wrap'),
        spacing = "5",
        align = "center",
        min_height ="85vh",
    )
    return base_page(my_child)


