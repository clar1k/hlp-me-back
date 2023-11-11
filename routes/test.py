from fastapi import APIRouter
from models.user import InputBotUser
from config.database import db
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/')
def test():
    db.user.insert_one({'name': 'test'})
    return JSONResponse({'msg': 'test'}, 200)


@router.post('/bot/create/user')
def create_bot_user(user: InputBotUser):
    db.user.insert_one(user.model_dump())
    return JSONResponse({'msg': 'User added'}, 200)
