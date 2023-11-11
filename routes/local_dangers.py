from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.location import LocationRequest
from config.database import db


router = APIRouter(prefix='/local/dangers')


@router.post('/create')
def get_alerts(location: LocationRequest):
    db.dangers.insert_one(location.model_dump())
    return JSONResponse({'msg': 'Added new danger to the local dangers'}, 200)
