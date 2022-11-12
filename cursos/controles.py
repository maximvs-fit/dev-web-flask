from flask import render_template

from cursos import cursos_bp


@cursos_bp.route('/')
def get_contato():
    return render_template('cursos.html')
