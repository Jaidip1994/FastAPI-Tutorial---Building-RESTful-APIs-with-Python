from uuid import UUID, uuid4
from fastapi import FastAPI
from typing import List
from models import Gender, Role, User

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
