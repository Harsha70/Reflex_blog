import reflex as rx
from datetime import datetime, timezone
import sqlalchemy
from sqlmodel import Field, Relationship
from .. import utils
from reflex_local_auth.user import LocalUser


class UserInfo(rx.Model, table= True):
    email:str
    user_id: int = Field(foreign_key='localuser.id')
    user: LocalUser | None = Relationship()
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={'server_default': sqlalchemy.func.now()},
        nullable=False
        )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={'onupdate': sqlalchemy.func.now(),
                          'server_default': sqlalchemy.func.now()},
        nullable=False
        )
    # created_from_ip: str