from sqlalchemy import Column, Integer, VARCHAR, DateTime
from datetime import datetime

from database import Base

class Board(Base):
  __tablename__="Board"
  
  no = Column(Integer, primary_key=True, autoincrement=True)
  writer = Column(VARCHAR(30), nullable=False)
  title = Column(VARCHAR(30), nullable=False)
  content = Column(VARCHAR(100), nullable=False)
  date = Column(DateTime, nullable=False, default=datetime.now)
  del_yn = Column(VARCHAR(1), nullable=False, default='Y')


class User(Base):
  __tablename__ = "Users"
  
  user_no = Column(Integer, primary_key=True, autoincrement=True)
  user_name = Column(VARCHAR(10), nullable=False)
  email= Column(VARCHAR(100), nullable=False, unique=True)
  hashed_pw=Column(VARCHAR(100), nullable=False)
  role=Column(VARCHAR(20), nullable=False, default='MEMBER')
  status=Column(VARCHAR(1), nullable=False, default='1')
  regdate = Column(DateTime, nullable=False, default=datetime.now)


class Data(Base):
  __tablename__ = "Data"

  no = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(VARCHAR(512), nullable=False, default='name')
  title = Column(VARCHAR(30), nullable=False, default='title')
  content = Column(VARCHAR(512), nullable=False, default='content')
  date = Column(DateTime, nullable=False, default=datetime.now)