from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import Gender, Role, User, UserUpdaterequest

app = FastAPI()
db: List[User] = [
    User(
        id=UUID("3776f209-4074-4d23-9329-feb62a2bb4a6"),
        firstName="Jai",
        lastName="Ghosh",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("78b13896-9416-4a82-8938-c70ca79f998c"),
        firstName="Sas",
        lastName="Bha",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]


@app.get(path="/")
async def root():
    return {"Hello": "World"}


@app.get(path="/api/v1/users")
async def fetch_users():
    return db


@app.post(path="/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exist'
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user: UserUpdaterequest):
    for usr in db:
        if usr.id == user_id:
            usr.firstName = user.firstName if user.firstName else usr.firstName
            usr.lastName = user.lastName if user.lastName else usr.lastName
            usr.middleName = user.middleName if user.middleName else usr.middleName
            usr.roles = user.roles if user.roles else usr.roles
            return 
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exist'
    )
