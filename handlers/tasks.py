from fastapi import APIRouter
from starlette import status

import fixtures
from fixtures import *
from schema.task import Task

router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    '/all',
    response_model=list[Task]
)
async def get_tasks():
    return tasks, status.HTTP_200_OK

@router.post(
    '/',
    response_model=Task
)
async def create_task(body : Task):
    fixtures.tasks.append(body)
    return body, status.HTTP_201_CREATED