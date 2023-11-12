from datetime import datetime

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class LocationRequest(BaseModel):
    name: str
    description: str
    coordinates: Coordinates
    access_token: str = Field(..., alias='accessToken')
    date_time: datetime
    time: datetime
