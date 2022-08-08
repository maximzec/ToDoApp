from unicodedata import name
from sqlalchemy.orm import Session

import models.task, schemas.task_schema


def create_task(db:Session, task: models.task):
    db_task = schemas.task_schema.Task(
        name = task.name,
        status = schemas.task_schema.TaskStatuses.opened
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_all_tasks(db:Session):
    return db.query(schemas.task_schema.Task).all()

