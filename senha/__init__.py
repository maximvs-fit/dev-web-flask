from flask import Blueprint

senha_bp = Blueprint(
    'senha',
    __name__,
    template_folder='templates'
)

from . import controles
