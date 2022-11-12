from flask import Blueprint

contato_bp = Blueprint(
    'contato',
    __name__,
    template_folder='templates'
)

from . import controles
