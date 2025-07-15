from fastapi_users import schemas
from typing import Optional
from datetime import datetime
from enum import Enum

class RoleEnumStr(str, Enum):
    admin = "admin"
    editor = "editor"

class UserBase(schemas.BaseUserCreate):
    name: str
    age: int
    role: RoleEnumStr = RoleEnumStr.editor
    activated: bool = True

class UserCreate(UserBase):
    password: str  # deja este și în BaseUserCreate, dar poți suprascrie dacă vrei

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str]
    age: Optional[int]
    role: Optional[RoleEnumStr]
    activated: Optional[bool]

class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    age: int
    role: RoleEnumStr
    created_at: datetime
    activated: bool

    class Config:
        orm_mode = True
