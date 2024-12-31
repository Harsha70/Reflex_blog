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
    user_id : int | None=None
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
    
