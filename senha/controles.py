import uuid

from flask import (make_response, redirect, render_template, request, session,
                   url_for)

from senha import senha_bp


@senha_bp.route('/')
def get_home():
    id_sessao = request.cookies.get('id_sessao')
    sessao = session.get(id_sessao)
    print(sessao)

    if sessao is None:
        print('usuário não autenticado, redirecionando...')
        return redirect(url_for('.get_login'))

    print(f'GET: O cookie enviado pelo navegador é: {id_sessao}')
    return render_template('senha.html')


@senha_bp.route('/', methods=['POST'])
def post_home():
    id_sessao = request.cookies.get('id_sessao')
    print(f'POST: O cookie enviado pelo navegador é: {id_sessao}')
    senha_atual = session.get('senha', 0)
    session.update(senha=senha_atual+1)
    msg = f'Olá {request.form["x"]}, sua senha é {session["senha"]}!'

    return render_template('senha.html', msg=msg)


@senha_bp.route('/login')
def get_login():
    return render_template('teste-cookie.html')


@senha_bp.route('/login', methods=['POST'])
def post_login():
    id_sessao = str(uuid.uuid1())  # cria a chave da sessão
    nome = request.form['nome']
    sessao = {'usuario': nome}
    # salva os dados pertinentes à aplicação no
    session.update({id_sessao: sessao})
    # objeto de sessão do flask

    resposta = make_response(redirect(url_for('.get_home')))
    resposta.set_cookie('id_sessao', id_sessao)
    return resposta


@senha_bp.route('/logout', methods=['get'])
def logout():
    id_sessao = request.cookies.get('id_sessao')
    session.pop(id_sessao, None)

    resposta = make_response(redirect(url_for('.get_login')))
    resposta.set_cookie('id_sessao', '')
    return resposta
