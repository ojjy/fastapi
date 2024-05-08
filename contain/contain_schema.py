from pydantic import BaseModel
from datetime import datetime

"""
crud를 하기 위한 schema crud함수는 이 schema를 바라보고 해당하는 연산 수행
"""
class NewContain(BaseModel):
  name: str
  title: str
  content: str


class ContainList(BaseModel):
  no: int
  name: str
  title: str
  date: datetime


class Contain(BaseModel):
  no: int
  name: str
  title: str
  content: str
  date: datetime
