from http.client import HTTPResponse
from fastapi import FastAPI, Depends
from schemas import CreateTaskModel
from database_models import Task

from sqlalchemy.orm import Session
from crud import create_task, get_all_tasks
from database import SessionLocal, engine

from database import Base

Base.metadata.create_all(bind=engine)

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
    return 'Hello, world!'


#@app.post('/Tasks')
#async def create_task(task:Task):
#   return task


@app.post('/tasks/create-task')
async def create_task_route(task:CreateTaskModel, db:Session = Depends(get_db)):
    return create_task(task=task, db=db)

@app.get('/tasks/all')
async def get_all_tasks_route(db:Session = Depends(get_db)):
    return get_all_tasks(db=db)

