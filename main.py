from fastapi import FastAPI
from models.task import Task

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello, world!'


@app.post('/Tasks')
async def create_task(task:Task):
    return task