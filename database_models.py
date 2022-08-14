from telnetlib import STATUS
from venv import create
from sqlalchemy import Column, Integer, Enum, String, DateTime
from database import Base
import enum



#Task Status = Создано, Закрыто
class TaskStatuses(enum.Enum):
    opened = 0
    closed = 1

#Таблица для хранения задач
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(Enum(TaskStatuses))
    create_date = Column(DateTime)


