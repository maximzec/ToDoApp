from pydantic import BaseModel

class CreateTaskModel(BaseModel):
    name:str
    description:str
    

