from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import db
from models.location import LocationRequest
from schemas.dangers import danger_entity

router = APIRouter(prefix='/local/dangers')


@router.post('/create')
async def create_alert(location: LocationRequest):
    # input datetime
    try:
        db.dangers.insert_one(location.model_dump())
    except Exception as e:
        return JSONResponse({'msg': str(e)}, 500)
    return JSONResponse({'msg': 'Added new danger to the local dangers'}, 200)


@router.get(
    ''
)  # With the dangers fetch the user, who creted the danger and return in the response
async def get_all_dangers():
    dangers = db.dangers.find()
    response = list(dangers)

    for index in range(len(response)):
        response[index] = await danger_entity(response[index])
    print(response)
    return JSONResponse(response, 200)
