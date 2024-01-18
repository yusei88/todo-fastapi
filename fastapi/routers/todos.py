from fastapi import APIRouter

router = APIRouter()

@router.get("/todos")
async def get_tasks():
    pass


@router.post("/todos")
async def post_task():
    pass


@router.put("/todos")
async def put_task():
    pass


@router.delete("/todos")
async def delete_task():
    pass
