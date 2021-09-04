from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = [
    {
        'id': '0',
        'responsavel': 'Gustavo',
        'tarefa': 'Desenvolver APIs',
        'status': 'Concluida',
    },
    {
        'id':'1',
        'responsavel': 'Caique',
        'tarefa': 'Arquitetura Back-End',
        'status': 'Pendente'
    }
]


# DEVOLVE LISTA DE TAREFAS E PERMITE ADICIONAR NOVA TAREFA

@app.route('/tarefa/', methods=['GET', 'POST'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])

    elif request.method == 'GET':
        return jsonify(tarefas)


# DEVOLVE E DELETA UMA TAREFA PELO ID

@app.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id] 
        except IndexError:
            mensagem = f'Tarefa de id {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status':'erro', 'mensagem': mensagem}
        return jsonify(response)

# ALTERA O STATUS DA TAREFA, NENHUMA OUTRA ALTERAÇÃO É PERMITIDA ALÉM DO STATUS

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        if dados['responsavel'] != tarefas[id]['responsavel']:
            mensagem = 'Apenas o STATUS da tarefa pode ser alterado'
            response = {'status':'erro', 'mensagem': mensagem}
            return response
        if dados['tarefa'] != tarefas[id]['tarefa']:
            mensagem = 'Apenas o STATUS da tarefa pode ser alterado'
            response = {'status':'erro', 'mensagem': mensagem}
            return response
        else:
            tarefas[id] = dados
            return "registro alterado"

    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro deletado'})


if __name__ == '__main__':
    app.run(debug=True)