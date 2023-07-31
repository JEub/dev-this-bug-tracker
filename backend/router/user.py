from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from model.user import User

router = APIRouter()


class RequestBody(BaseModel):
    email: str
    username: str
    password: str


@router.get("/")
def getAllUsers(db: Session = Depends(get_db)):
    userList = db.query(User).all()
    return userList


@router.get("/{id}")
def getUserById(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    return user


@router.post("/create")
def createUser(user: RequestBody, db: Session = Depends(get_db)):
    model = User(email=user.email, username=user.username, password=user.password)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


@router.put("/update/{id}")
def updateUser(id: int, user: RequestBody, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).update(
        {
            User.email: user.email,
            User.username: user.username,
            User.password: user.password,
        }
    )
    db.commit()
    return user


@router.delete("/delete/{id}")
def deleteUser(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user
