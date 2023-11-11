from jose import jwt
import bcrypt
from bson import ObjectId
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Body
from models.users import UserIn, User
from config.database import db
from config.config import Config
from schemas.users import userEntity


users = APIRouter(tags=['Users'])


@users.get('/user/{user_id}')
def get_user(user_id: str):
    _id = ObjectId(user_id)
    user = db.user.find_one({'id': _id})
    return userEntity(user)


@users.post('/user/')
def create_user(user: UserIn):
    if db.user.find_one(dict(user)):
        return JSONResponse({'message': 'User is already in database'}, 400)
    new_user = User.parse_obj(user)
    password = new_user.password.encode('utf-8')
    new_user.password = bcrypt.hashpw(password)
    db.user.insert_one(new_user, dict())
    return JSONResponse({'message': 'User has been created'}, 201)


@users.put('/user/')
def update_user(user: UserIn):
    _filter = {'email': user.email}
    update_values = {'$set': user.dict()}
    is_updated_document = db.user.find_one_and_update(_filter, update_values)
    if is_updated_document:
        return JSONResponse({'message': 'Update successful'}, 201)
    return JSONResponse({'message': 'Could not find a user with this email'}, 400)


@users.delete('/user/')
async def delete_user(token: dict = Body(..., example={'token': 'access token value'})):
    decoded_token = jwt.decode(token['token'], Config.SECRET_KEY, ['HS256'])
    _id = ObjectId(decoded_token['_id'])
    if db.user.find_one_and_delete({'_id': id}):
        return JSONResponse({'message': 'Success!'}, 200)
    return JSONResponse({'message': 'User does not exist'}, 400)