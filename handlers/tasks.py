from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/task", tags=["task"])

@router.get('/all')
async def get_tasks():
    return {'message': 'ok'}

@router.post('/')
async def create_task():
    return {'message': 'app is working'}

class DecodePostRequest(BaseModel):
    text : str

@router.post('/test')
async def create_test(post : DecodePostRequest):
    return {"message" : post.text}