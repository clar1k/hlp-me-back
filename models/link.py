from datetime import datetime

from pydantic import BaseModel, Field


class LinkRequest(BaseModel):
    name: str
    descriptrion: str
    link: str
    access_token: str = Field(..., alias='accessToken')
    time: datetime = datetime.utcnow()
