from sqlalchemy.orm import Session
from src.database.models import Livro

def obter_todos(db: Session):
    return db.query(Livro).all()

def obter_por_id(db: Session, id: int):
    return db.query(Livro).filter(Livro.id == id).first()

def cadastrar(db: Session, livro: Livro):
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro

def apagar(db: Session, id: int):
    livro = obter_por_id(db, id)
    if not livro:
        return 0
    db.delete(livro)
    db.commit()
    return 1
