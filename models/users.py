from datetime import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.utcnow()


class UserIn(BaseModel):
    tg_id: int
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    username: str
    email: EmailStr


class UserUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    accessToken: str


def check_password(password: str, hashed_password: str) -> bool:
    return password == hashed_password
