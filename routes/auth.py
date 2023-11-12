from datetime import datetime, timedelta

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jose import jwt

from config.config import Config
from config.database import db
from models.users import TelegramUserInput, UserIn
from schemas.users import user_entity

auth = APIRouter(tags=['Auth'])


@auth.post('/tg/register')
async def register_telegram_user(user: TelegramUserInput):
    if db.user.find_one({'user_id': user.user_id}):
        return JSONResponse({'msg': 'User already registered'}, 400)

    try:
        db.user.insert_one(user.model_dump())
    except Exception as e:
        print(e)
        return JSONResponse({'msg': 'Error when connecting to the database'}, 400)

    return JSONResponse({'msg': 'User registered'}, 200)


@auth.post('/tg/login')
async def login_telegram_user(user: TelegramUserInput):
    user = db.user.find_one({'user_id': user.user_id})
    if not user:
        return JSONResponse({'msg': 'User not found'}, 404)

    payload_data = {'_id': user['_id']}
    access_token = jwt.encode(payload_data, 'secret')

    response = {
        'access_token': access_token,
        'token_type': 'Bearer',
        'msg': 'Login successful',
    }
    return JSONResponse(response, 200)


@auth.put('/tg/update')
async def update_telegram_user_info(user_update: TelegramUserInput):
    user = db.user.find_one({'user_id': user_update.user_id})
    if not user:
        return JSONResponse({'msg': 'User not found'}, 404)

    db.user.update_one(
        {'user_id': user_update.user_id}, {'$set': user_update.model_dump()}
    )
    return JSONResponse({'msg': 'Update successful'}, 200)
