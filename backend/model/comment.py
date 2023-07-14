from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from database import Base

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    body = Column(String, nullable=False)
    creator = Column(Integer, ForeignKey("user.id"))
    created_date = Column(DateTime)
    visible = Column(bool)
    last_update = Column(DateTime)
    publish_date = Column(DateTime)