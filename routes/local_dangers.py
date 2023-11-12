from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import db
from models.location import LocationRequest
from schemas.dangers import danger_entity
from schemas.users import user_entity

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
        print(response[index])
        user = db.user.find_one({'user_id': response[index]['user_id']})
        user = user_entity(user)
        response[index]['user'] = user

    return JSONResponse(response, 200)


@router.get('/my/{user_id}')
async def get_my_dangers(user_id: int):
    user_dangers = db.dangers.find({'user_id': user_id})
    user_dangers = list(user_dangers)
    for index in range(len(user_dangers)):
        user_dangers[index] = await danger_entity(user_dangers[index])

    print(user_dangers)
    return JSONResponse(user_dangers, 200)
