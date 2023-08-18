from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from model.user import User
import logging

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

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


# Authentication
SECRET_KEY = "secret" ## change to env variable later
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
    # username or email
    if "@" in username:
        user = db.query(User).filter(User.email == username).first()
    else:
        user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/create")
def createUser(user: RequestBody, db: Session = Depends(get_db)):
    model = User(
        email=user.email,
        username=user.username,
        password=get_password_hash(user.password),
    )
    #check if user with same username or email exists
    if db.query(User).filter(User.username == user.username).first() or db.query(User).filter(User.email == user.email).first():
        return {"error": "User already exists"}
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

@router.post("/login", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    ## log request body
    logging.info(form_data)
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "username": user.username}