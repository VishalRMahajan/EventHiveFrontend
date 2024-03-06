from sqlalchemy import Column, Integer, String
from database import Base, engine


class Student(Base):
    __tablename__ = "student"

    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, primary_key=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class Committee(Base):
    __tablename__ = "committee"

    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, primary_key=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String, index=True, nullable=False)


Base.metadata.create_all(bind=engine)
