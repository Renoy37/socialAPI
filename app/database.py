from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import Settings
import time

SQLALCHEMY_DATABASE_URL = f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     # Connecting to database
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapitutor',
#                                 user='postgres', password='RenonAdmin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connection To Database Was Succesful")
#         break
#     except Exception as error:
#         print("Connection to Database failed")
#         print("Error:", error)
#         time.sleep(2)
