import datetime


from sqlalchemy import Integer, Boolean, text, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import mapped_column, Mapped
from typing import Annotated, List


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column("id", Integer, primary_key=True, autoincrement=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        default=text("TIMEZONE('utc', now())"))]

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[intpk]
    telegram_id: Mapped[int] = mapped_column('telegram_id', Integer,
                                            autoincrement=False)
    
    is_subscribed = mapped_column(Boolean, default=False)
    
    tasks: Mapped[List['Task']] = relationship('Task', back_populates='user')
    
    def __str__(self) -> str:
        return f"TgId: {self.telegram_id} | Subscribed: {self.is_subscribed}"
    

class Task(Base):
    __tablename__ = "task"
    
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    is_active = mapped_column(Boolean, default=False)
    description: Mapped[str] = mapped_column("description", String(length=500), nullable=True, default="")
    
    user: Mapped['User'] = relationship('User', back_populates='tasks')
    user_id = mapped_column(Integer, ForeignKey(column='user.id'))
    
    def __str__(self) -> str:
        return f"Id: {self.id} | Status: {self.is_active} | UserId: {self.user_id}"
