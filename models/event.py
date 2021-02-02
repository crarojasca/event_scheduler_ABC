from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    place = db.Column(db.String(100))
    adress = db.Column(db.String(1000))
    start = db.Column(db.Date())
    end = db.Column(db.Date())
    