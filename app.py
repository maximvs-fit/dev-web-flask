# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    msg = ''
    if request.method == 'POST':
        msg = f'Olá {request.form["x"]}, sua senha é 23!'

    print(dict(request.form))
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)