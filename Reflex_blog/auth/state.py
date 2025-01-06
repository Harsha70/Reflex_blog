import reflex as rx
import reflex_local_auth
from ..model import UserInfo

from typing import Optional

import sqlmodel

class SessionState(reflex_local_auth.LocalAuthState):
    # @rx.cached_var
    
    @rx.var(cache=True)
    def my_userinfo_id(self) -> int:
        if self.authenticated_user_info is None:
            return None
        return self.authenticated_user_info.id
    
    @rx.var(cache=True)
    def my_user_id(self) -> int:
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.id
    
    @rx.var(cache=True)
    def authenticated_user_info(self) -> Optional[UserInfo]:
        if self.authenticated_user.id < 0:
            return None
        with rx.session() as session:
            result =  session.exec(
                sqlmodel.select(UserInfo).where(
                    UserInfo.user_id == self.authenticated_user.id
                ),
            ).one_or_none()
            # result.user
            if result is None:
                return None
            # user_info = result.user
            # print(result.user)
            return result
    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.authenticated_user_info)
    
    def perform_logout(self):
        self.do_logout()
        return rx.redirect('/')

class MyRegisterState(reflex_local_auth.RegistrationState):
    # This event handler must be named something besides `handle_registration`!!!
    def handle_registration_email(self, form_data):
        
        registration_result = self.handle_registration(form_data)
        
        if self.new_user_id >= 0:
            print(self.new_user_id)
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        # created_from_ip=self.router.headers.get(
                        #     "x_forwarded_for",
                        #     self.router.session.client_ip,
                        # ),
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
        return registration_result

