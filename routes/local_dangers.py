from bson import ObjectId
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import db
from models.location import LocationRequest
from schemas.dangers import danger_entity
from schemas.users import user_entity

router = APIRouter(prefix='/local/dangers')


@router.delete('/delete/{danger_id}')
def delete_danger_by_unique_id(danger_id: str):
    object_id = ObjectId(danger_id)
    db.dangers.find_one_and_delete({'_id': object_id})
    return JSONResponse({'msg': 'Successfully deleted danger'}, 200)


@router.delete('/{danger_name}')
def delete_danger_by_name(danger_name: str):
    db.dangers.find_one_and_delete({'name': danger_name})
    return JSONResponse({'msg': 'Successfully deleted danger'}, 200)


@router.post('/create')
async def create_alert(location: LocationRequest):
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
