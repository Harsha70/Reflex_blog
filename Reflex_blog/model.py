import reflex as rx
from datetime import datetime, timezone
import sqlalchemy
from sqlmodel import Field, Relationship
from . import utils
from reflex_local_auth.user import LocalUser
from typing import Optional, List

class UserInfo(rx.Model, table= True):
    email:str
    user_id: int = Field(foreign_key='localuser.id')
    posts: List['BlogPostModel'] = Relationship(back_populates='userinfo')
    contact_entries: List['ContactEntryModel'] = Relationship(back_populates='userinfo')
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
    

class BlogPostModel(rx.Model, table=True):
    # user
    userinfo_id: int = Field(foreign_key='userinfo.id')
    userinfo: Optional[UserInfo] = Relationship(back_populates='posts')
    title: str
    content: str
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
    publish_active: bool = False
    publish_date: datetime = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
        )


class ContactEntryModel(rx.Model, table=True):
    user_id : int | None=None
    userinfo_id: int = Field(foreign_key='userinfo.id')
    userinfo: Optional[UserInfo] = Relationship(back_populates='contact_entries')
    first_name: str
    last_name: str | None=None
    email: str = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={'server_default': sqlalchemy.func.now()},
        nullable=False
        )
    
