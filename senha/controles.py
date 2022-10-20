from senha import senha_bp
from flask import render_template, session, request


@senha_bp.route('/')
def get_home():
    print('chamou o get')
    return render_template('index.html')


@senha_bp.route('/', methods=['POST'])
def post_home():
    print('chamou o post')
    senha_atual = session.get('senha', 0)
    session.update(senha=senha_atual+1)
    msg = f'Olá {request.form["x"]}, sua senha é {session["senha"]}!'

    return render_template('index.html', msg=msg)
