from flask import render_template, request

from contato import contato_bp


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
