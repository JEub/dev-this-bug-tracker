from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from model.comment import Comment
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class RequestBody(BaseModel):
    ticket_id: int
    creator: int
    body: str
    created_date: str
    visible: int
    last_update: str
    publish_date: str


@router.get("/all")
def getAllComments(db: Session = Depends(get_db)):
    return db.query(Comment).all()

@router.get("/{ticket_id}")
def getComments(ticket_id: int, db: Session = Depends(get_db)):
    return db.query(Comment).filter(Comment.ticket_id == ticket_id).all()

@router.post("/create")
def createComment(comment: RequestBody, db: Session = Depends(get_db)):
    model = Comment(
        ticket_id=comment.ticket_id,
        creator=comment.creator,
        body=comment.body,
        created_date=datetime.now(),
        visible=comment.visible,
        last_update=datetime.now(),
        publish_date=datetime.now()
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

@router.put("/update/{comment_id}")
def updateComment(comment_id: int, comment: RequestBody, db: Session = Depends(get_db)):
    db.query(Comment).filter(Comment.id == comment_id).update(comment.dict())
    db.commit()
    return db.query(Comment).filter(Comment.id == comment_id).first()

@router.delete("/delete/{comment_id}")
def deleteComment(comment_id: int, db: Session = Depends(get_db)):
    db.query(Comment).filter(Comment.id == comment_id).delete()
    db.commit()
    return {"message": "Comment deleted successfully."}