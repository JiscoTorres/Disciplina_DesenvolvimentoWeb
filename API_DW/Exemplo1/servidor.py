import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
# 1. Definimos o tipo de objeto que nossa API irá expor.
# As anotações de tipo (str, int) são usadas para gerar o schema GraphQL.
@strawberry.type
class Autor:
    id: int
    nome: str

@strawberry.type
class Livro:
    id: int
    titulo: str
    autor: Autor

# --- "Banco de Dados" em memória ---
db_livros = [
    Livro(id=1, titulo="O Senhor dos Anéis", autor=Autor(id=1, nome="J.R.R. Tolkien")),
    Livro(id=2, titulo="Harry Potter", autor=Autor(id=2, nome="JK Rowling")),
    Livro(id=3, titulo="Duna", autor=Autor(id=3, nome="Frank Herbert")),
]

 
 # --- Definição dos Tipos GraphQL com Strawberry ---
# 2. Definimos a "Query", que são os pontos de entrada para consulta de dados.
@strawberry.type
class Query:
# Este resolver retorna uma lista de todos os livros.
    @strawberry.field
    def livros(self) -> List[Livro]:
        return [livro for livro in db_livros]
# Este resolver busca um único livro por seu ID.

# Ele aceita um argumento 'livro_id' e pode retornar um Livro ou None.

    @strawberry.field
    def livro(self, livro_id: int) -> Optional[Livro]:
        for livro_data in db_livros:
            if livro_data.id == livro_id:
                return livro_data
            return None


    @strawberry.field
    def livro(self, nome: str) -> List[Livro]:
        lista = []
        for livro in db_livros:
            if livro.autor.nome.lower().find(nome.lower()) >= 0:
                 lista.append(livro) #Se encontrar dentro da string a variavel nome, retorna isso    
            return lista




# --- Configuração do Servidor ---
# 3. Criamos o schema GraphQL com a nossa Query.
schema = strawberry.Schema(query=Query)
# 4. Criamos a rota GraphQL usando o Strawberry e o FastAPI.
graphql_app = GraphQLRouter(schema)
# 5. Criamos a aplicação FastAPI principal e incluímos a rota GraphQL.
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")




#AGORA ABRIR O LINK http://127.0.0.1:8000/graphql para rodar o projeto