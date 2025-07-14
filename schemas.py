from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserUpdate(UserBase):
    pass

class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

    class Config:
        from_attributes = True

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
