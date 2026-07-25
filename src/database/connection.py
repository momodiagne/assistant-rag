import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base

os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///data/database.sqlite"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Création de la base"""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
