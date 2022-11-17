from flask import render_template, request

from contato import contato_bp

import json


@contato_bp.post('/usuario')
def teste_ajax():
    dados = request.json
    print(type(dados))
    print(dados)

    dicionario = {
        'resposta1': True,
        'resposta2': 25,
        'resposta3': [1, 2, 3],
        'resposta4': 'olá mundo!'
    }
    return json.dumps(dicionario)

@contato_bp.get('/html')
def teste_ajax_html():
    return render_template('teste-ajax.html')


@contato_bp.route('/')
def get_contato():
    return render_template('contato.html')


@contato_bp.route('/', methods=['POST'])
def post_contato():
    form = dict(request.form)
    print(form)
    msg = (f'Olá {form.get("nome").split()[0]}, '
           'recebemos sua mensagem e em breve alguém '
           'da nossa equipe entrará em contato.')
    return render_template('contato.html', msg=msg)
