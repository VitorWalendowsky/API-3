from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# TODO: utilizar vaiavel de ambiente ou arquivo .env
# não é a forma correta de fazer
DATABASE_URL = "mysql+pymysql://root:admin@127.0.0.1:3306/mercado"

engine = create_engine(url=DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


