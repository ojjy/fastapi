from fastapi import FastAPI
from sqlalchemy import create_engine, text
engine= create_engine('mysql+pymysql://fastapi:Fastapi*0691@10.10.151.46/fastapidb')

with engine.connect() as conn:
    rs = conn.execute(text('SELECT KEY_VALUE FROM GCUNIV_KEY;')).fetchall()
    if ('37050452106c8f1e57f2c61ca6dedc3d7ef01eab2d6e05f5c12af17a000322ca',)in rs:

        print(True)
        True
    else:
        False
