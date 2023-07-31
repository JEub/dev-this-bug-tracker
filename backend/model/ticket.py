from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text

from config.database import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(DateTime)
    completed_date = Column(DateTime)
    status_id = Column(Integer, ForeignKey("status.id"))
    story_points = Column(Integer)
    creator = Column(Integer, ForeignKey("user.id"))
    created_date = Column(DateTime)
    last_update = Column(DateTime)
