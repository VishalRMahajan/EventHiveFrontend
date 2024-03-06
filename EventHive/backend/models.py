from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine


class User(Base):
    __tablename__ = "users"

    pid = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String, index=True, nullable=False)


Base.metadata.create_all(bind=engine)
