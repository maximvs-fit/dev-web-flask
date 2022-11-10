from flask import render_template

from login import login_bp


@login_bp.route('/')
def login_teste():
    return render_template('pasta1/login.html')
