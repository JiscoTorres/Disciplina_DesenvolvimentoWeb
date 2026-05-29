# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# BD_TAREFAS
tarefas = [
    {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Lavar carro', 'concluida': False},
    {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Fazer Projeto', 'concluida': False},
    {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Limpar Casa', 'concluida': True}
]

# Rota principal
@app.route("/")
def index():
    return "<h1>Exemplos de envio de parâmetros com Flask!</h1>"


# --- EXEMPLOS DA AULA ---

# Exemplo 1: Parâmetros na URL
@app.route("/usuario/<string:nome>")
def saudar_usuario(nome):
    return f"<h1>Olá, {nome}!</h1><p>Este parâmetro foi recebido pela URL.</p>"

# Exemplo 2: Query String
@app.route("/pesquisa")
def pesquisar():
    termo_busca = request.args.get('q')
    if termo_busca:
        return f"<h1>Você pesquisou por: '{termo_busca}'</h1>"
    else:
        return "<h1>Por favor, forneça um termo de busca. Ex: /pesquisa?q=python</h1>"

# Exemplo 3: Formulário de Login (GET e POST)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        return f"<h1>Login Tentado!</h1><p>Usuário: {usuario}</p>"
    return """
    <h1>Formulário de Login</h1>
    <form method="post">
        <label>Usuário:</label><br>
        <input type="text" name="usuario"><br><br>
        <label>Senha:</label><br>
        <input type="password" name="senha"><br><br>
        <input type="submit" value="Entrar">
    </form>
    """

# Exemplo 4: POST com JSON
@app.route("/api/produtos", methods=['POST'])
def criar_produto():
    dados = request.get_json()
    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    nome_produto = dados['nome']
    preco_produto = dados['preco']
    return jsonify({
        "mensagem": "Produto recebido com sucesso!",
        "produto_recebido": {"nome": nome_produto, "preco": preco_produto}
    }), 201


# --- EXERCÍCIO: API REST DE TAREFAS ---

# GET /tarefas → retorna todas as tarefas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200


# GET /tarefas/<id> → retorna uma tarefa pelo id
@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def buscar_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa), 200


# POST /tarefas → cria uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    if not dados or 'titulo' not in dados or 'descricao' not in dados:
        return jsonify({"erro": "Campos 'titulo' e 'descricao' são obrigatórios"}), 400

    novo_id = max(t['id'] for t in tarefas) + 1 if tarefas else 1
    nova_tarefa = {
        'id': novo_id,
        'titulo': dados['titulo'],
        'descricao': dados['descricao'],
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


# PUT /tarefas/<id> → atualiza uma tarefa existente
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    dados = request.get_json()
    if 'titulo' in dados:
        tarefa['titulo'] = dados['titulo']
    if 'descricao' in dados:
        tarefa['descricao'] = dados['descricao']
    if 'concluida' in dados:
        tarefa['concluida'] = dados['concluida']

    return jsonify(tarefa), 200


# DELETE /tarefas/<id> → remove uma tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefas.remove(tarefa)
    return jsonify({"mensagem": f"Tarefa {tarefa_id} deletada com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
