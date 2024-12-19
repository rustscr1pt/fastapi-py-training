from fastapi import APIRouter

import fixtures
from fixtures import *
from schema.task import Task

router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    '/all',
    response_model=list[Task]
)
async def get_tasks():
    return tasks

@router.post(
    '/',
    response_model=Task
)
async def create_task(body : Task):
    fixtures.tasks.append(body)
    return body