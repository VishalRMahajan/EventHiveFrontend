import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes


def init_connection_pool(connector: Connector) -> Engine:
    """Create a connection pool to the database"""
    def getconn():
        """Return a connection to the database"""
        load_dotenv()  # Load the environment variables
        conn = connector.connect(
            os.getenv("CONNECTION_NAME"),
            "pg8000",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            db=os.getenv("DB_NAME"),
            ip_type=IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
        return conn

    sqlalchemy_database_url = "postgresql+pg8000://"

    con = "postgresql://vishal:993uhp!_-b9dQjD@35.200.156.179:5432/eventhive-db"

    engine = create_engine(con)
    return engine


connector = Connector()

engine = init_connection_pool(connector)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Get a database connection to the database using a context manager"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
