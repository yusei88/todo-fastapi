from fastapi import APIRouter
from typing import List

from api.schemas.response_todo import ResponseToDo

router = APIRouter()


@router.get("/todos", response_model=List[ResponseToDo])
async def get_tasks():
    return [ResponseToDo(todo_id=1, title="1つ目")]


@router.post("/todos", response_model=ResponseToDo)
async def post_task():
    ResponseToDo(todo_id=1, title="1つ目")


@router.put("/todos", response_model=ResponseToDo)
async def put_task():
    ResponseToDo(todo_id=1, title="1つ目")


@router.delete("/todos", response_model=ResponseToDo)
async def delete_task():
    ResponseToDo(todo_id=1, title="1つ目")
