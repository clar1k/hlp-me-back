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