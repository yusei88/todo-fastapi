from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class ResponseToDo(BaseModel):
    todo_id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    finished: bool = Field(False, description="完了フラグ")
    due_date: Optional[datetime] = Field(None)

