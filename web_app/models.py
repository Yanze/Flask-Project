from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(80), unique=True)
    email = db.Column('email', db.String(45), unique=True)
    password = db.Column('pwd', db.String(255))

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

