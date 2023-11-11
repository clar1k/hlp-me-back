from fastapi import APIRouter
from config.database import db
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def test():
    db.user.insert_one({"name": "test"})
    return JSONResponse({"msg": "test"}, 200)
