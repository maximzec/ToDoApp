from sqlalchemy.orm import Session
from database_models import Task, TaskStatuses
from schemas import CreateTaskModel, UpdateTaskModel, DeleteTaskModel
from datetime import datetime


def create_task(db:Session, task: CreateTaskModel):
    db_task = Task(
        name = task.name,
        description = task.description,
        status = TaskStatuses.opened,
        create_date = datetime.now()
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db:Session, updated_task: UpdateTaskModel):
    filtered_task = {k:v for k,v in updated_task.to_dict().items() if v is not None}
    db.query(Task).filter(Task.id==updated_task.id).update(filtered_task)
    db.commit()
    return updated_task

def delete_task(db:Session, delete_task: DeleteTaskModel):
    db.query(Task).filter(Task.id==delete_task.id).delete(synchronize_session=False)
    db.commit()
    return delete_task



def get_all_tasks(db:Session):
    return db.query(Task).all()

