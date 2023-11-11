import io
from datetime import datetime, timedelta
from typing import Dict
import bcrypt
from jose import jwt
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.users import UserIn, User, check_password
from config.database import db
from config.config import Config

auth = APIRouter(tags=['Auth'])

@auth.post('/auth/register')
async def register(user: UserIn):
    user_is_existed = db.user.find_one({'email': user.email})
    if user_is_existed:
        return JSONResponse({'message': 'User is already in db'}, 400)
    db.user.insert_one({'user': user.model_dump()})
    return JSONResponse({'message': 'User has been added to database!'})


@auth.post('/auth/login')
async def login(user_input: UserIn) -> JSONResponse:
    return login_user(user_input)

def login_user(user_input: UserIn) -> JSONResponse:
    user = db.user.find_one({'email': user_input.email})
    if user:
        if check_password(user_input.password, user['password']):
            unique_id = str(user['_id'])
            token = create_token(unique_id)
            return JSONResponse({'accessToken': token, 'message': 'Success!'}, 200)
        return JSONResponse({'message': 'Incorrect password'}, 400)
    return JSONResponse({'message': 'User is not found'}, 400)


async def create_token(unique_id: str) -> str:
    expiration_time = datetime.utcnow() + timedelta(days=2)
    token = jwt.encode({'_id': unique_id, 'exp': expiration_time}, Config.SECRET_KEY)
    return token


@auth.post('/auth/logout/{token}')
async def logout(token: str) -> JSONResponse:
    if db.token_blacklist.find_one({'token': token}):
        return JSONResponse({'message': 'Token is already in db'}, 400)

    db.token_blacklist.insert_one({'token': token})
    return JSONResponse({'message': 'Logout successful'}, 200)