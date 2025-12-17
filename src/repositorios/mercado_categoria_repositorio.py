# from src.banco_dados import conectar
from sqlalchemy.orm import Session

from src.database.models import Categoria


def cadastrar(db: Session, nome: str):
    categoria = Categoria(nome=nome)
    db.add(categoria) #insert into categorias (nnome) values (%s)
    db.commit() # concretização categoria no banco
    db.refresh(categoria) # atribuir para a categoria o ID que foi gerado no bd
    return categoria


    # Abrir a conexão com o banco de dados
#    conexao = conectar()
    # Criando um cursor para poder executar comandos no bd
#    cursor = conexao.cursor()
    # Definir qual comando será executado
#    sql = "INSERT INTO categorias (nome) VALUES (%s)"
#    dados = (nome,)

#    cursor.execute(sql, dados)

    # Confirmar o comando (concretizar o comando de insert)
#    conexao.commit()

    # Fechar a conexão com o banco de dados do cursor
#    cursor.close()


def editar(id: int, nome: str):
    conexao = conectar()

    cursor = conexao.cursor()
    
    sql = "UPDATE categorias SET nome = %s WHERE id = %s"
    dados = (nome, id)
    cursor.execute(sql, dados)
    
    conexao.commit()

    linhas_afetadas = cursor.rowcount

    cursor.close()

    conexao.close()
    return linhas_afetadas


def apagar(db: Session, id: int) -> int:
    #Busca a categoria pelo ID (retorna a primeira encontrada ou none)
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    #Se não encontrou a categoria:
    if not categoria:
        return 0 #retornamos 0 indicando que nenhuma linha foi afetada
    #Se encontrou, deletamos a categoria
    db.delete(categoria)
    db.commit()
    return 1 #retornamos 1 indicando que uma linha foi afetada


    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "DELETE FROM categorias WHERE id = %s"
    # dados = (id,)
    # cursor.execute(sql, dados)
    # conexao.commit()

    # linhas_afetadas = cursor.rowcount

    # cursor.close()
    # conexao.close()
    # return linhas_afetadas

def obter_todos(db: Session):
    categorias = db.query(Categoria).all()
    return categorias


    # conexao = conectar()

    # cursor = conexao.cursor()

    # cursor.execute("SELECT id, nome  FROM categorias")

    # registros = cursor.fetchall()

    # cursor.close()
    # conexao.close()
    # categorias = []

    # for registro in registros:
    #     categoria = {
    #         "id": registro[0],
    #         "nome": registro[1]
    #     }
    #     categorias.append(categoria)

    # return categorias


def obter_por_id(db: Session, id: int):
    categoriga = db.query(Categoria).filter(Categoria.id == id).first()
    return categoriga

    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "SELECT id, nome FROM categorias WHERE id = %s"
    # dados = (id,)
    # cursor.execute(sql, dados)

    # registro = cursor.fetchone()
    # if not registro:
    #     return None

    # return {
    #     "id": registro[0],
    #     "nome": registro[1]
    # }
