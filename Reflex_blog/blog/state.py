from datetime import datetime
from typing import List, Optional
import reflex as rx

from .model import BlogPostModel
from sqlmodel import select

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    post_content: str = ""
    post_publish_active: bool = False

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
            if result is None:
                self.post_content = ""
                return
            self.post_content = self.post.content
            self.post_publish_active = self.post.publish_active
            
    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel).where(BlogPostModel.publish_active==True)
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
            self.post = post
    
    def to_blog_post(self):
        if not self.post:
            return rx.redirect('/blog')
        return rx.redirect(f'/blog/{self.post.id}')

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}

    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)
        return self.to_blog_post()
        # redirect
        
class BlogEditPostFormState(BlogPostState):
    form_data: dict = {}
    # content: str = ''

    @rx.var
    def publish_display_date(self)->str:
        if not self.post:
            return datetime.now().strftime("%Y-%m-%d")
        if not self.post.publish_date:
            return datetime.now().strftime("%Y-%m-%d")
        return self.post.publish_date.strftime("%Y-%m-%d")
        # return datetime.today().strftime('%Y-%m-%d')
    
    @rx.var
    def publish_display_time(self)->str:
        if not self.post:
            return datetime.now().strftime("%H:%M:%S")
        if not self.post.publish_date:
            return datetime.now().strftime("%H:%M:%S")
        return self.post.publish_date.strftime("%H:%M:%S")
        # return datetime.now().strftime('%H:%M:%S')
    
    def handle_submit(self, form_data):
        self.form_data = form_data
        post_id = form_data.pop('post_id')
        publish_date=None
        if 'publish_date' in form_data:
            publish_date = form_data.pop('publish_date')
        publish_time = None
        if 'publish_time' in form_data:
            publish_time = form_data.pop('publish_time')
        publish_input_string = f'{publish_date} {publish_time}'
        print('publish_input_string', publish_input_string)
        final_publish_date = None
        try:
            final_publish_date = datetime.strptime(publish_input_string, '%Y-%m-%d %H:%M:%S')
        except :
            final_publish_date = None
        print(final_publish_date)
        publish_active = False
        if 'publish_active' in form_data:
            publish_active = form_data.pop('publish_active') == 'on'
        updated_data = {**form_data}
        updated_data['publish_active'] = publish_active
        updated_data['publish_date'] = final_publish_date
        self.edit_post(post_id, updated_data)
        return self.to_blog_post()
        
        # redirect
        # print(post_id, updated_data)








