from . import db
from flask_login import UserMixin
from ..login_manager import login_manager

    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))
