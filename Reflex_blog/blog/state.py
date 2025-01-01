from typing import List, Optional
import reflex as rx

from .model import BlogPostModel
from sqlmodel import select

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    post_content: str = ""

    @rx.var
    def blog_post_id(self)->str:
        return self.router.page.params.get('blog_id', "")

    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id =="":
                self.post = None
                return
            result = session.exec(
                select(BlogPostModel).where(BlogPostModel.id == self.blog_post_id)
            ).one_or_none()
            self.post = result
            self.post_content = self.post.content
            
    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result

    def add_post(self, form_data: dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding",post)
            session.add(post)
            session.commit()
            session.refresh(post)
            # print("added",post)
            self.post = post

    # def get_post(self, post_id):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPostModel)
    #         )
    #         self.posts = result 

    def edit_post(self, post_id:int, updated_data: dict):
        
        with rx.session() as session:
            post = session.exec(
                select(BlogPostModel).where(BlogPostModel.id == post_id)
            ).one_or_none()
            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value)
                
            session.add(post)
            session.commit()
            session.refresh(post)
            
            # post = BlogPostModel(**form_data)
            # # print("adding",post)
            # session.add(post)
            # session.commit()
            # session.refresh(post)
            # # print("added",post)
            # self.post = post

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}

    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)
        # redirect
        
class BlogEditPostFormState(BlogPostState):
    form_data: dict = {}
    # content: str = ''

    def handle_submit(self, form_data):
        self.form_data = form_data
        post_id = form_data.pop('post_id')
        updated_data = {**form_data}
        self.edit_post(post_id, updated_data)
        # redirect
        # print(post_id, updated_data)








