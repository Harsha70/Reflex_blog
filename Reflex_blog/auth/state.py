import reflex as rx
import reflex_local_auth
from .models import UserInfo

from typing import Optional

import sqlmodel

class SessionState(reflex_local_auth.LocalAuthState):
    @rx.var(cache=True)
    def authenticated_user_info(self) -> Optional[UserInfo]:
        if self.authenticated_user.id < 0:
            return
        with rx.session() as session:
            return session.exec(
                sqlmodel.select(UserInfo).where(
                    UserInfo.user_id == self.authenticated_user.id
                ),
            ).one_or_none()
    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.authenticated_user_info)

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

