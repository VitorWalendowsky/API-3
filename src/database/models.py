from sqlalchemy import Column, Date, Double, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# teemos uma classe chamada Catetgoria que herda as prioriades e metodos da base
class Categoria(Base):
    __tablename__ = "categorias"

# Coluna dda PK id to dipo inteiro auto incrementavel
    id = Column(Integer, primary_key=True, autoincrement=True)
# Coluna do nome que não permite nulo
    nome = Column(String(255), nullable=False)

class Clientes(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)
    limite = Column(Double, nullable=True)
    