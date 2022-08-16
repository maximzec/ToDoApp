from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

#Task routes dto's
class CreateTaskModel(BaseModel):
    name:str
    description:str
    

class UpdateTaskModel(BaseModel):
    id: int
    name:Optional[str]
    description:Optional[str]

    def to_dict(self):
        return {
            'name':self.name,
            'description': self.description
        }