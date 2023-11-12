from datetime import datetime

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class LocationRequest(BaseModel):
    user_id: int = 0
    name: str
    description: str
    coordinates: Coordinates
    access_token: str = Field(..., alias='accessToken')
    date_time: datetime = datetime.utcnow()
