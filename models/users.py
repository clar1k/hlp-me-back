from datetime import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.utcnow()


class UserIn(BaseModel):
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


class TelegramUserInput(BaseModel):
    tg_id: int
    username: str = ''
    first_name: str
    hash_str: str


def check_password(password: str, hashed_password: str) -> bool:
    return password == hashed_password
