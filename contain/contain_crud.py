from sqlalchemy.orm import Session
from sqlalchemy import and_

from models import Data
from contain.contain_schema import NewContain, ContainList, Contain

def insert_contain(new_contain: NewContain, db: Session):
    data = Data(
        name = new_contain.name,
        title = new_contain.title,
        content = new_contain.content,
    ) 
    db.add(data)
    db.commit()

    return data.no

def list_all_contain(db: Session):
  lists = db.query(Data).all()
  return [ContainList(no=row.no, name=row.name, title=row.title, date=row.date) for row in lists]

def get_contain(contain_no: int, db: Session):
  try:
      contain = db.query(Data).filter(and_(Data.no == contain_no)).first()
      return Contain(no=contain.no, name=contain.name, title=contain.title, content=contain.content, date=contain.date)
  except Exception as e:
     return {'error': str(e), 'msg': '존재하지 않는 데이터 번호'}
#
# def update_post(update_post: UpdatePost, db: Session):
#   post = db.query(Board).filter(and_(Board.no == update_post.no, Board.del_yn == 'Y')).first()
#   try:
#     if not post:
#       raise Exception("존재하지 않는 게시글 번호입니다.")
#
#     post.title = update_post.title
#     post.content = update_post.content
#     db.commit()
#     db.refresh(post)
#     return get_post(post.no, db)
#
#   except Exception as e:
#     return str(e)
#
#
# def alter_del_yn(post_no: int, db: Session):
#    post = db.query(Board).filter(and_(Board.no == post_no, Board.del_yn == 'Y')).first()
#    try:
#     if not post:
#        raise Exception("존재하지 않는 게시글 번호입니다")
#
#     post.del_yn = 'N'
#     db.commit()
#     db.refresh(post)
#     return {'msg':'삭제가 완료되었습니다.'}
#    except Exception as e:
#     return str(e)
#
#
# def delete_post(post_no: int, db: Session):
#    post = db.query(Board).filter(and_(Board.no == post_no, Board.del_yn == 'Y')).first()
#    try:
#     if not post:
#        raise Exception("존재하지 않는 게시글 번호입니다")
#     db.delete(post)
#     db.commit()
#     return {'msg':'삭제가 완료되었습니다.'}
#    except Exception as e:
#     return str(e)
#
