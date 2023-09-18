from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from model.status import Status

router = APIRouter()

class RequestBody(BaseModel):
    name: str

@router.get("/all")
def getAllStatus(db: Session = Depends(get_db)):
    return db.query(Status).all()

@router.get("/{status_id}")
def getStatus(status_id: int, db: Session = Depends(get_db)):
    return db.query(Status).filter(Status.id == status_id).first()

@router.post("/create")
def createStatus(status: RequestBody, db: Session = Depends(get_db)):
    model = Status(name=status.name)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

@router.put("/update/{status_id}")
def updateStatus(status_id: int, status: RequestBody, db: Session = Depends(get_db)):
    db.query(Status).filter(Status.id == status_id).update(status.dict())
    db.commit()
    return db.query(Status).filter(Status.id == status_id).first()

@router.delete("/delete/{status_id}")
def deleteStatus(status_id: int, db: Session = Depends(get_db)):
    db.query(Status).filter(Status.id == status_id).delete()
    db.commit()
    return {"message": "Status deleted successfully."}