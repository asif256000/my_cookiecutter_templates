from flask import Blueprint

bp = Blueprint("main", __name__)

from {{cookiecutter.flask_app}}_app_pkg.main import routes
