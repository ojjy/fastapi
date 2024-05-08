from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn
import models
from database import engine
models.Base.metadata.create_all(bind=engine)
from pathlib import Path

from board import board_router
from user import user_router
from contain import contain_router
import boto3

# from common import key
app = FastAPI()

# app.include_router(board_router.app, tags=["board"])
# app.include_router(user_router.app, tags=["user"])
app.include_router(contain_router.app, tags=["contain"])

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
#app.mount("/static", StaticFiles(directory="static"), name="static")/


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/file/store", response_class=HTMLResponse)
async def upload_file(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/file/store", response_class=HTMLResponse)
async def store_file(request: Request, file: UploadFile=File(...)):

    try:
        contents = file.file.read()
        with open("uploaded_" + file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

if __name__ == "__main__":
    uvicorn.run('main:app',reload=True, host='0.0.0.0', port=8080)