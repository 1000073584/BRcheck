from sqlalchemy import Boolean, Column, Float, Integer, String
from db.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    
    test = Column(String(50), nullable=False)