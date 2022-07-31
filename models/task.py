from pydantic import BaseModel

class Task(BaseModel):
    name:str
    status: int = 0

