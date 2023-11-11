import bcrypt
from bson import ObjectId
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from jose import jwt

from config.config import Config
from config.database import db
from models.users import User, UserIn, UserUpdate
from schemas.users import user_entity

users = APIRouter(tags=['Users'])


@users.get('/user/{user_id}')
def get_user(user_id: str):
    _id = ObjectId(user_id)
    user = db.user.find_one({'id': _id})
    return user_entity(user)


@users.post('/user/')
def create_user(user: UserIn):
    if db.user.find_one(dict(user)):
        return JSONResponse({'message': 'User is already in database'}, 400)
    new_user = User.parse_obj(user)
    password = new_user.password.encode('utf-8')
    new_user.password = bcrypt.hashpw(password)
    db.user.insert_one(new_user, dict())
    return JSONResponse({'message': 'User has been created'}, 201)


@users.put('/user/update')
async def update_user(user_id: int, user_update: UserUpdate) -> JSONResponse:
    # З UserUpdate декодувати токен, і потім беремо ObjectId, і за ним знаходимо користувача в базі
    user = db.user.find_one({'_id': id})

    if user is None:
        return JSONResponse({'message': 'User is not found'}, 400)
    user_data = {
        'full_name': user_update.full_name,
        'email': user_update.email,
        'phone_number': user_update.phone_number,
        'accessToken': user_update.accessToken,
    }

    db.user.update_one({'_id': user_id}, {'$set': user})

    return JSONResponse(
        {
            'username': user_data['username'],
            'email': user_data['email'],
            'phone_number': user_data['phone_number'],
            'accessToken': user_data['decoded_token'],
        },
        200,
    )


@users.delete('/user/')
async def delete_user(token: dict = Body(..., example={'token': 'access token value'})):
    decoded_token = jwt.decode(token['token'], Config.SECRET_KEY, ['HS256'])
    _id = ObjectId(decoded_token['_id'])
    if db.user.find_one_and_delete({'_id': id}):
        return JSONResponse({'message': 'Success!'}, 200)
    return JSONResponse({'message': 'User does not exist'}, 400)
