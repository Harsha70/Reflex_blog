import reflex as rx
import time
import asyncio
from .. import navigations
from ..ui.base import base_page
from sqlmodel import Field
from datetime import datetime, timezone

import sqlalchemy

def get_utc_now()->datetime:
    return datetime.now(timezone.utc)
    
class ContactEntryModel(rx.Model, table=True):
    first_name: str
    last_name: str | None=None
    email: str = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={'server_default': sqlalchemy.func.now()},
        nullable=False
        )
    


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5
    
    @rx.var
    def timeleftlabel(self) -> str:
        if self.timeleft<1:
            return 'No time left'
        return f'{self.timeleft} seconds'
    
    @rx.var
    def thank_you(self)->str:
        first_name = self.form_data.get('first_name') or ''
        return f'thank you, {first_name}'
    
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        data = {}
        for k, v in form_data.items():
            if v == '' or v == None:
                continue
            data[k] = v
        
        with rx.session() as session:
            df_entry = ContactEntryModel(
                **data
            )
            session.add(df_entry)
            session.commit()
            
            self.did_submit =True
            yield            
        
        await asyncio.sleep(2)
        self.did_submit = False
        yield
        
    # async def start_timer(self):
    #     while self.timeleft < 100:
    #         await asyncio.sleep(1)
    #         self.timeleft += 1
    #         yield

@rx.page(route=navigations.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        type="text",
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.input(
                    type="email",
                    name="email",
                    width="100%",
                    plactholder = "Email Address"
                ),
                rx.text_area(
                    name='message', 
                    placeholder="Message",
                    required=True,
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        )
    my_child = rx.vstack(
        rx.heading("Contact Us", size = "9"),
        rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
        rx.desktop_only(rx.box(my_form, width = "50vw")),
        rx.mobile_only(rx.box(my_form, width = "95vw")),
        rx.tablet_only(rx.box(my_form, width = "75vw")),
        spacing = "5",
        justify = "center",
        align = "center",
        min_height ="85vh",
        id = "my_child"
    )
    return base_page(my_child)