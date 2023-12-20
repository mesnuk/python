from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from app.film_api.views import FilmController, FilmsController

film_api_bp = Blueprint('film', __name__, url_prefix='/api/film')

api = Api(film_api_bp, errors=film_api_bp.errorhandler)
api.add_resource(FilmController, '/<int:id>', '/')
api.add_resource(FilmsController, 's')


@film_api_bp.errorhandler(ValidationError)
def handler(e):
    return jsonify(e.messages), 400
