from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def connect_db() -> Session:
    engine = create_engine()
    session = Session(bind=engine.connect())
    return session