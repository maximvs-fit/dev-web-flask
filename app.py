# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session


app = Flask(__name__)

app.secret_key = b'52fb96da04fe19cb18b8a5831459be41c7dabf7dd3253e2b7609032579b5c181'


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


if __name__ == '__main__':
    app.run(debug=True)