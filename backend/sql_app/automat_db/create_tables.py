from core.database import engine, Base

def create_tables():
    Base.metadata.create_all(engine)