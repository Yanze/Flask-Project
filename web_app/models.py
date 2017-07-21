from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(80), unique=True)
    email = db.Column('email', db.String(45), unique=True)
    password = db.Column('pwd', db.String(255))


    """
    user_loader callback is used to reload the user object from the user Id stored in the session
    it returns the corresponding user object, otherwise return None if Id is not valid
    """
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def __init__(self, username, email, password, id=None):
        self.username = username
        self.email = email
        self.password = password
        self.id = id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_user_by(username):
        user = User.query.filter_by(username=username).first()
        return user




class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    content = db.Column('content', db.String(140))
    username = db.Column('username', db.String(140))
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)

    def __init__(self, content, user_id, username=username, id=None):
        self.user_id = user_id
        self.content = content
        self.username = username
        self.created_at = datetime.now()
        self.id = id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        messages = Message.query.all()
        return messages


class Comment(db.Model):
    __tablename__ = 'comments'    
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    message_id = db.Column('message_id', db.Integer, db.ForeignKey('messages.id'))
    content = db.Column('content', db.String(140))
    username = db.Column('username', db.String(140))
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)

    def __init__(self, content, user_id, message_id, username=username, id=None):
        self.content = content
        self.user_id = user_id
        self.message_id = message_id
        self.username = username
        self.created_at = datetime.now()
        self.id = id


    def save(self):
        db.session.add(self)
        db.session.commit()  

    @staticmethod
    def get_all():
        comments = Comment.query.all()
        return comments      