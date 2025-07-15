# models/user.py
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum
from uuid import uuid4
from datetime import datetime
import enum
from sqlalchemy.orm import DeclarativeBase

class RoleEnum(enum.Enum):
    admin = "admin"
    editor = "editor"

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    name = Column(String, nullable=False)  # numele utilizatorului
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.editor)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    activated = Column(Boolean, default=True, nullable=False)  # activat sau nu


