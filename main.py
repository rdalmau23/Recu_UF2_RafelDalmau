from fastapi import FastAPI
from services import *
from services.delete_user import delete_user
from services.get_users import get_users

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/get", response_model=list[dict])
async def users_get():
    result = get_users()
    return result

@app.delete("/users/delete/{user_id}", response_model=list[dict])
async def users_delete():
    result = delete_user()
    return result

@app.post("/users/modify", response_model=list[dict])
async def user_modify():
    result = user_modify()
    return result