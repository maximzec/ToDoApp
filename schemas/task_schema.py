from telnetlib import STATUS
from sqlalchemy import Column, Integer, Enum, String
from database import Base
import enum

class TaskStatuses(enum.Enum):
    opened = 0
    closed = 1


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Enum(TaskStatuses))


