# DB connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings  # we'll define this in config.py

# PostgreSQL URL format:
# "postgresql://username:password@localhost:5432/dbname"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
