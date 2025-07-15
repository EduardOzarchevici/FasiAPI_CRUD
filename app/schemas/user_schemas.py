from pydantic import BaseModel
from fastapi_users import schemas
from typing import Optional
from datetime import datetime
from enum import Enum
from uuid import UUID

class RoleEnum(str, Enum):
    admin = "admin"
    editor = "editor"

class UserBase(BaseModel):
    name: str
    email: str
    role: RoleEnum = RoleEnum.editor
    activated: bool = True
    password: str

class UserUpdate(UserBase):
    pass

class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[RoleEnum] = None
    activated: Optional[bool] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: UUID
    name: str
    email: str
    role: RoleEnum
    created_at: datetime
    activated: bool

    class Config:
        from_attributes = True


class UserRead(schemas.BaseUser[UUID]):
    name: str
    role: RoleEnum
    created_at: datetime
    activated: bool

class UserCreate(schemas.BaseUserCreate):
    name: str
    role: RoleEnum
    activated: bool = True

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str] = None
    role: Optional[RoleEnum] = None
    activated: Optional[bool] = None
