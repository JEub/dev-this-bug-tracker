from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from database import Base

class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_date = Column(DateTime)
    last_update = Column(DateTime)