import reflex as rx
import asyncio
from typing import List
from sqlmodel import select
from .model import ContactEntryModel

class ContactState(rx.State):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []
    did_submit: bool = False
    timeleft: int = 5
    
    # @rx.var
    # def timeleftlabel(self) -> str:
    #     if self.timeleft<1:
    #         return 'No time left'
    #     return f'{self.timeleft} seconds'
    
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

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(select(ContactEntryModel)).all()
            self.entries = entries
            # print(entries)
