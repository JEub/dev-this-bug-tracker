from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from model.ticket import Ticket

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


@router.get("/")
def getAllTickets(db: Session = Depends(get_db)):
    ticketList = db.query(Ticket).all()
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


@router.delete("delete/{id}")
def deleteTicket(id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    db.delete(ticket)
    db.commit()
    return ticket
