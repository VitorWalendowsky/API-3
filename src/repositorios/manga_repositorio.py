from sqlalchemy.orm import Session
from src.database.models import Manga

def listar(db: Session):
    return db.query(Manga).all()

def criar(db: Session, manga: Manga):   
    db.add(manga)
    db.commit()
    db.refresh(manga)
    return manga
