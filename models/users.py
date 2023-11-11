from datetime import datetime
import bcrypt
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.utcnow()


class UserIn(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    nickname: str
    email: EmailStr


def check_password(password: str, hashed_password: str) -> bool:
    hashed_input = bcrypt.hashpw(password.encode("utf-8"))
    return hashed_input == hashed_password