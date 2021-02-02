import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import DB_URI


engine = create_engine(DB_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

