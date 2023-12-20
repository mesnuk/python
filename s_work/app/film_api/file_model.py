from app import db


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(100))
    year = db.Column(db.String(4))
    director = db.Column(db.String(20))