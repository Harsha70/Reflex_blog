import reflex as rx
import reflex_local_auth
from .models import UserInfo

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
