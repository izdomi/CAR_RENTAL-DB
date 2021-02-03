import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import DB_URI


engine = create_engine(DB_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class Client(Base):
    __tablename__ = "client"

    id=Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String(30), nullable=False)
    last_name=Column(String(30), nullable=False)
    license_number=Column(String(20),nullable=False)
    address=Column(String(100), nullable=False)
    phone=Column(String(10),nullable=False)
    email=Column(String(15), nullable=True)
    login_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    loout_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __str__(self):
        return f"{self.id} {self.first_name_name} {self.last_name}"

    def __repr__(self):
        return f"Client(id={self.id}, first_name={self.first_name!r}, last_name={self.last_name})"


