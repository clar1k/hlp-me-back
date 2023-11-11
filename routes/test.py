from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import db
from models.user import InputBotUser

router = APIRouter()


@router.post('/bot/create/user')
def create_bot_user(user: InputBotUser):
    db.user.insert_one(user.model_dump())
    return JSONResponse({'msg': 'User added'}, 200)
