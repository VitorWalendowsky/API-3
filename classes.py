from pydantic import BaseModel


class AlunoCalcularMedia(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nome_completo: str


class CategoriaCriar(BaseModel):
    nome: str


class CategoriaEditar(BaseModel):
    nome: str


class ProdutoCriar(BaseModel):
    nome: str
    id_categoria: int


class ProdutoEditar(BaseModel):
    nome: str
    id_categoria: int
