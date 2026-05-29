# app.py
from flask import Flask, request, jsonify
# Inicializa a aplicação Flask
app = Flask(__name__)
# --- EXEMPLOS ABAIXO ---
#BD_TAREFAS
tarefas = [
     {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Lavar carro', 'concluida': False},
     {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Fazer Projeto', 'concluida': False},
     {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Limpar Casa', 'concluida': True}
]




# Rota principal para referência
@app.route("/")
def index():
    return "<h1>Exemplos de envio de parâmetros com Flask!</h1>"

@app.route("/tarefas", method=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200


# ... cole os códigos dos exemplos aqui ...



# O if __name__ == '__main__': não é necessário ao usar 'flask run',
# mas é uma boa prática para rodar com 'python app.py'
if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")

