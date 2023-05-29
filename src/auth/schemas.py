from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    role_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "role_name": "chef, manager, customer"
            }
        }


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
