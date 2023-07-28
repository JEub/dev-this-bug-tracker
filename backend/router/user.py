from fastapi import APIRouter
from config.database import get_db
from pydantic import BaseModel
from model.user import User

router = APIRouter()

class RequestBody(BaseModel):
    email: str
    username: str
    password: str

@router.get("/")
def getAllUsers():
    with get_db() as db:
        userList = db.query(User).all()
    return userList

@router.get("/{id}")
def getUserById(id: int):
    with get_db() as db:
        user = db.query(User).filter(User.id == id).first()
    return user

@router.post("/")
def createUser(user: RequestBody):
    with get_db() as db:
        model = User(email=user.email, username=user.username, password=user.password)
        db.add(model)
        db.commit()
        db.refresh(model)
    return model

@router.put("/{id}")
def updateUser(id: int, user: RequestBody):
    with get_db() as db:
        model = User(email=user.email, username=user.username, password=user.password)
        db.query(User).filter(User.id == id).update(model)
        db.commit()
        db.refresh(user)
    return user