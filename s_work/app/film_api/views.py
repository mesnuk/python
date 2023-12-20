from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app import db
from app.film_api.file_model import Film
from app.film_api.schemas import FilmsSchema


class FilmController(Resource):
    @jwt_required()
    def get(self, id):
        film = Film.query.get(id)
        if not film:
            return {
                "message": "NOT FOUNDDDDDDDDDDDDDDD"
            }, 404
        schema = FilmsSchema()
        return schema.dump(film)

    @jwt_required()
    def post(self):
        schema = FilmsSchema()
        film = schema.load(request.json)
        db.session.add(film)
        db.session.commit()

        return schema.dump(film), 201

    @jwt_required()
    def put(self, id):
        film = Film.query.get(id)
        if not film:
            return {
                "message": "NOT FOUNDDDDDDDDDDDDDDD"
            }, 404
        schema = FilmsSchema()
        film = schema.load(request.json, instance=film)
        db.session.commit()
        return schema.dump(film), 200

    @jwt_required()
    def delete(self, id):
        film = Film.query.get(id)
        if not film:
            return {
                "message": "NOT FOUNDDDDDDDDDDDDDDD"
            }, 404
        db.session.delete(film)
        db.session.commit()
        return {}, 204


class FilmsController(Resource):
    @jwt_required()
    def get(self):
        films = Film.query.all()
        schema = FilmsSchema(many=True)
        return schema.dump(films)
