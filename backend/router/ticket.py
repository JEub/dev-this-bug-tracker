from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from model.ticket import Ticket
from model.user import User
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import logging

router = APIRouter()

class RequestBody(BaseModel):
    title: str
    description: Optional[str]
    start_date: str
    completed_date: Optional[str]
    status_id: Optional[int]
    story_points: int
    creator: int
    created_date: str
    last_update: str


class TicketBuilder:
    def __init__(self, requestBody: RequestBody):
        self.title = requestBody.title

        if requestBody.description != None and requestBody.description != "":
            self.description = requestBody.description
        else:
            self.description = None

        self.start_date = datetime.strptime(requestBody.start_date, "%m/%d/%Y %H:%M:%S")

        if requestBody.completed_date != None and requestBody.completed_date != "":
            self.completed_date = datetime.strptime(
                requestBody.completed_date, "%m/%d/%Y %H:%M:%S"
            )
        else:
            self.completed_date = None

        if requestBody.status_id != None and requestBody.status_id != "":
            self.status_id = requestBody.status_id
        else:
            self.status_id = None

        self.story_points = requestBody.story_points
        self.creator = requestBody.creator
        self.created_date = datetime.strptime(
            requestBody.created_date, "%m/%d/%Y %H:%M:%S"
        )
        self.last_update = datetime.strptime(
            requestBody.last_update, "%m/%d/%Y %H:%M:%S"
        )

    def build(self):
        return Ticket(
            title=self.title,
            description=self.description,
            start_date=self.start_date,
            completed_date=self.completed_date,
            status_id=self.status_id,
            story_points=self.story_points,
            creator=self.creator,
            created_date=self.created_date,
        )

SECRET_KEY = "secret" ## change to env variable later
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"

class Token(BaseModel):
    username: str

def getUserFromToken(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = Token(username=username)
        user = db.query(User).filter(User.username == token_data.username).first()
        if user is None:
            raise credentials_exception
        return user.username
    except JWTError:
        return None

# get ticket list by user id
@router.get("/")
def getAllTickets(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    ## get user data from token and get user id
    ## user_id = get_user_id_from_token(token)
    user = getUserFromToken(db, token)
    ticketList = db.query(Ticket).filter(Ticket.creator == User.id).all()
    return ticketList


@router.get("/{id}")
def getTicketById(id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    return ticket


@router.post("/create")
def createTicket(ticket: RequestBody, db: Session = Depends(get_db)):
    model = TicketBuilder(ticket).build()
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


@router.put("/update/{id}")
def updateTicket(id: int, ticket: RequestBody, db: Session = Depends(get_db)):
    model = TicketBuilder(ticket).build()
    db.query(Ticket).filter(Ticket.id == id).update(model)
    db.commit()
    db.refresh(model)
    return model


@router.delete("/delete/{id}")
def deleteTicket(id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    db.delete(ticket)
    db.commit()
    return ticket
