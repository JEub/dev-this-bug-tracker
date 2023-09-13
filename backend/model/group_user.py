from sqlalchemy import Column, Integer, DateTime, ForeignKey

from config.database import Base


class GroupUser(Base):
    __tablename__ = "group_user"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"), primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
