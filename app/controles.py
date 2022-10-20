from flask import render_template, session, request
from . import app


@app.route('/')
def get_home():
    print('chamou o get')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post_home():
    print('chamou o post')
    senha_atual = session.get('senha', 0)
    session.update(senha=senha_atual+1)
    msg = f'Olá {request.form["x"]}, sua senha é {session["senha"]}!'

    return render_template('index.html', msg=msg)
