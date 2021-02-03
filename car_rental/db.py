import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, TIMESTAMP, ForeignKey, Numeric
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
    logout_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    client_with_car=relationship("Car", foreign_keys="Car.id",back_populates="client_id")

    def __str__(self):
        return f"{self.id} {self.first_name_name} {self.last_name}"

    def __repr__(self):
        return f"Client(id={self.id}, first_name={self.first_name!r}, last_name={self.last_name})"

class Car(Base):
    __tablename__ = "car"

    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(30), nullable=False)
    description=Column(String(500), nullable=False)
    model=Column(String(30), nullable=False)
    year=Column(Integer, nullable=False)
    color=Column(String(30), nullable=False)
    capacity=Column(Integer, nullable=False)
    rate=Column(Numeric(2,1), nullable=True)
    client_id=relationship(Client,foreign_keys=[Client.id], back_populates="client_with_car")

    def _str_(self):
        return f"{self.id}. {self.name}"

    def _repr_(self):
        return f"Car(id={self.id}, name={self.name!r})"


