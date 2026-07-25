from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(String, primary_key=True)
    titre = Column(String, nullable=False)
    theme = Column(String)
    public_cible = Column(String)
    date_mise_a_jour = Column(DateTime)
    url_source = Column(String)
    
    chunks = relationship("Chunk", back_populates="document", cascade="all, delete-orphan")

class Chunk(Base):
    __tablename__ = 'chunks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    document_id = Column(String, ForeignKey('documents.id'), nullable=False)
    texte = Column(Text, nullable=False)
    position = Column(Integer, nullable=False) 
    nb_tokens = Column(Integer)
    
    document = relationship("Document", back_populates="chunks")

class UserQuery(Base):
    __tablename__ = 'user_queries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(Text, nullable=False)
    date_requete = Column(DateTime, default=datetime.utcnow)
