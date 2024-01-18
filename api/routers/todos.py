from typing import List
from datetime import datetime

from fastapi import APIRouter

import schemas.response_todo as todo_schema

router = APIRouter()


@router.get("/todos", response_model=List[todo_schema.ResponseToDo])
async def get_tasks():
    return [
        todo_schema.ResponseToDo(
            todo_id=1,
            title="1つ目",
            finished=False,
            due_date=datetime.now
        )
    ]


@router.post("/todos", response_model=todo_schema.ResponseToDo)
async def post_task():
    return todo_schema.ResponseToDo(
        todo_id=1,
        title="1つ目",
        finished=False,
        due_date=datetime.now
    )


@router.put("/todos", response_model=todo_schema.ResponseToDo)
async def put_task():
    return todo_schema.ResponseToDo(
        todo_id=1,
        title="1つ目",
        finished=False,
        due_date=datetime.now
    )


@router.delete("/todos", response_model=todo_schema.ResponseToDo)
async def delete_task():
    return todo_schema.ResponseToDo(
        todo_id=1,
        title="1つ目",
        finished=False,
        due_date=datetime.now
    )
