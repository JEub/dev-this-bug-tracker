from datetime import datetime
from fastapi import APIRouter
from config.database import get_db
from pydantic import BaseModel
from model.ticket import Ticket

router = APIRouter()

class RequestBody(BaseModel):
    title: str
    description: str
    start_date: datetime
    completed_date: datetime
    status_id: int
    story_points: int
    creator: int
    created_date: datetime
    last_update: datetime


@router.get("/")
def getAllTickets():
    with get_db() as db:
        ticketList = db.query(Ticket).all()
    return ticketList

@router.get("/{id}")
def getTicketById(id: int):
    with get_db() as db:
        ticket = db.query(Ticket).filter(Ticket.id == id).first()
    return ticket

@router.post("/")
def createTicket(ticket: RequestBody):
    with get_db() as db:
        model = Ticket(title=ticket.title, description=ticket.description, start_date=ticket.start_date, completed_date=ticket.completed_date, status_id=ticket.status_id, story_points=ticket.story_points, creator=ticket.creator, created_date=ticket.created_date, last_update=ticket.last_update)
        db.add(model)
        db.commit()
        db.refresh(model)
    return model

@router.put("/{id}")
def updateTicket(id: int, ticket: RequestBody):
    with get_db() as db:
        model = Ticket(title=ticket.title, description=ticket.description, start_date=ticket.start_date, completed_date=ticket.completed_date, status_id=ticket.status_id, story_points=ticket.story_points, creator=ticket.creator, created_date=ticket.created_date, last_update=ticket.last_update)
        db.query(Ticket).filter(Ticket.id == id).update(model)
        db.commit()
        db.refresh(model)
    return model

@router.delete("/{id}")
def deleteTicket(id: int):
    with get_db() as db:
        ticket = db.query(Ticket).filter(Ticket.id == id).first()
        db.delete(ticket)
        db.commit()
    return ticket
