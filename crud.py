from unicodedata import name
from sqlalchemy.orm import Session
from database_models import Task, TaskStatuses
from schemas import CreateTaskModel



def create_task(db:Session, task: CreateTaskModel):
    db_task = Task(
        name = task.name,
        status = TaskStatuses.opened
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_all_tasks(db:Session):
    return db.query(Task).all()

