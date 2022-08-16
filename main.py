from fastapi import FastAPI, HTTPException, Depends
from schemas import CreateTaskModel, UpdateTaskModel, DeleteTaskModel

from sqlalchemy.orm import Session
from crud import create_task, get_all_tasks, update_task, delete_task
from database import SessionLocal, engine

from database import Base


#Если отключить эту строчку, то чтобы редактировать базы нужны будут миграции
#Base.metadata.create_all(bind=engine)

#dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()



@app.get('/')
async def root():
    return 'Welcome to ToDoApp'

@app.post('/tasks/create-task')
async def create_task_route(task:CreateTaskModel, db:Session = Depends(get_db)):
    if task.name == "":
        raise HTTPException(status_code = 422, detail="Task name can't be empty")
    return create_task(task=task, db=db)

@app.put('/tasks/update-task')
async def update_task_route(updated_task: UpdateTaskModel, db:Session = Depends(get_db)):
    if updated_task.name is None and updated_task.description is None:
        raise HTTPException(status_code=422, detail='You must update at least one field')
    return update_task(db=db, updated_task=updated_task)


@app.delete('/tasks/delete-task')
async def delete_task_route(deleted_task:DeleteTaskModel, db:Session = Depends(get_db)):
    return delete_task(db=db, delete_task=deleted_task)

@app.get('/tasks/all')
async def get_all_tasks_route(db:Session = Depends(get_db)):
    return get_all_tasks(db=db)

