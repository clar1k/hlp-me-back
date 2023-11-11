from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class LocationRequest(BaseModel):
    name: str
    description: str
    danger_level: int = Field(..., alias='dangerLevel')
    coordinates: Coordinates
    access_token: str = Field(..., alias='accessToken')
