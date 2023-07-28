from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from config.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)