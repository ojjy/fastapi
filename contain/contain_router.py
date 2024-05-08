from sqlalchemy.orm import Session
from sqlalchemy import text, create_engine
from database import get_db

from fastapi import APIRouter, Depends, HTTPException, status

from contain import contain_crud, contain_schema

app = APIRouter(
    prefix="/contain",
)
# lists = db.query(Board).filter(Board.del_yn == 'Y').all()
@app.post(path="/add", description="데이터 생성")
async def create_new_cont(key: str, new_contain: contain_schema.NewContain, db: Session = Depends(get_db)):
    rs = db.execute(text('SELECT KEY_VALUE FROM GCUNIV_KEY;')).fetchall()
    if (key,) in rs:
        return contain_crud.insert_contain(new_contain, db)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid key")


@app.get(path="/list", description="전체 데이터 조회")
async def read_all_contain(key: str, db: Session = Depends(get_db)):
    rs = db.execute(text('SELECT KEY_VALUE FROM GCUNIV_KEY;')).fetchall()
    if (key,) in rs:
            return contain_crud.list_all_contain(db)
    else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid key")


@app.get(path="/read/{contain_no}", description="특정 데이터 조회")
async def read_contain(key: str, contain_no: int, db: Session = Depends(get_db)):
    rs = db.execute(text('SELECT KEY_VALUE FROM GCUNIV_KEY;')).fetchall()
    if (key,) in rs:
            return contain_crud.get_contain(contain_no, db)
    else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid key")
