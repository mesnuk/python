from marshmallow import fields, validate

from app import mm
from app.film_api.file_model import Film


class FilmsSchema(mm.SQLAlchemySchema):
    id = fields.Integer(required=False)
    name = fields.String(required=True, validate=[validate.Length(min=2, max=25)])
    description = fields.String(required=True, validate=[validate.Length(min=2, max=100)])
    year = fields.String(required=True, validate=[validate.Length(min=2, max=4)])
    director = fields.String(required=True, validate=[validate.Length(min=2, max=20)])

    class Meta:
        model = Film
        load_instance = True
