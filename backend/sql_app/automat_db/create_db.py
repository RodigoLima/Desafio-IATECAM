from core.database import SQLALCHEMY_DATABASE_URL,engine, Base
from sqlalchemy import create_engine,text
from sqlalchemy_utils import database_exists

def create_db():
    URL = "mysql+mysqlconnector://root:123@localhost:3306"
    if not database_exists(SQLALCHEMY_DATABASE_URL):
        engine_db = create_engine(URL)
        connection = engine_db.connect()
        statement = text("""CREATE DATABASE desafioiatecam""")
        connection.execute(statement)
        connection.commit()
