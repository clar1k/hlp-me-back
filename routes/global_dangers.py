from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import db
from models.link import LinkRequest
from schemas.global_dangers import global_danger_entity

router = APIRouter(prefix='/global/dangers')


@router.post('/create')
async def create_global_alert(link: LinkRequest):
    try:
        db.global_dangers.insert_one(link.model_dump())
    except Exception as e:
        return JSONResponse({'message': str(e)}, 400)
    return JSONResponse({'message': 'Added new danger to the global dangers!'}, 200)


@router.get('')
async def get_all_global_dangers():
    global_danger = db.global_dangers.find()
    response = list(global_danger)

    for i in range(len(response)):
        response[i] = await global_danger_entity(response[i])
    print(response)
    return JSONResponse(response, 200)
