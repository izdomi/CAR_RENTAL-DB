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
    address=Column(String(100), nullable=True)
    phone=Column(String(10),nullable=False)
    email=Column(String(15), nullable=True)
    login_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    logout_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    reservation = relationship("Reservation", back_populates="client")

    def __str__(self):
        return f"{self.id} {self.first_name_name} {self.last_name}"

    def __repr__(self):
        return f"Client(id={self.id}, first_name={self.first_name!r}, last_name={self.last_name})"



class Car_type(Base):
    __tablename__ = "car_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_label = Column(String(45), nullable=False)
    type_descr = Column(String(45), nullable=True)
    car = relationship("Car", back_populates="car_type")

    def __str__(self):
        return f"{self.id} {self.type_label}"

    def __repr__(self):
        return f"Car Type (id={self.id}, type_label={self.type_label})"

class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(50), nullable=False)
    city = Column(String(30), nullable=False)
    state = Column(String(30), nullable=False)
    car = relationship("Car", back_populates="location")
    reservation = relationship("Reservation", back_populates="location")
    def __str__(self):
        return f"{self.id} {self.street} {self.city}"

    def __repr__(self):
        return f" Car location (id = {self.id}, street={self.street})"


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
    currentlocation_id = Column(Integer, ForeignKey(Location.id),nullable=False)
    car_type_id = Column(Integer, ForeignKey(Car_type.id), nullable=False)
    reservation = relationship("Reservation", back_populates= "car")

    def __str__(self):
        return f"{self.id} {self.name}"

    def __repr__(self):
        return f"Car(id={self.id}, name={self.name!r})"

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    pickup_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)
    pickup_location_id = Column(Integer, ForeignKey(Location.id), nullable=False)
    return_location_id = Column(String(30), nullable=False)
    client_id = Column(Integer, ForeignKey(Client.id),nullable=False)
    car_id = Column(Integer,ForeignKey(Car.id), nullable=False)
