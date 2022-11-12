from flask import Flask
from contato import contato_bp
from cursos import cursos_bp

app = Flask(__name__)
app.config.from_object('app.config.Configuracao')

app.register_blueprint(contato_bp, url_prefix='/contato')
app.register_blueprint(cursos_bp, url_prefix='/cursos')
