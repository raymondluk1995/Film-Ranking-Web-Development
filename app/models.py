from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    administrator = db.Column(db.Boolean, default=False, nullable=False)
    preference = db.Column(db.String(300),index=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Poll(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    poll_name = db.Column(db.String(64),index=True,unique=True)
    category = db.Column(db.String(20),index=True)


    def __repr__(self):
        return '<Poll {}>'.format(self.poll_name)

class Option(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    poll_id = db.Column(db.Integer,db.ForeignKey('poll.id'))
    option = db.Column(db.String(50),index=True)
    votes = db.Column(db.Integer,default=0)

class Behaviour(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    poll_id = db.Column(db.Integer,db.ForeignKey('poll.id'),index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),index=True)
