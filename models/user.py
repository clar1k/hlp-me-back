from pydantic import BaseModel


class InputBotUser(BaseModel):
    full_name: str
    email: str
    phone_number: str
    username: str
