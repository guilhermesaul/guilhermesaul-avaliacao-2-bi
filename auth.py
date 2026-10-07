from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
