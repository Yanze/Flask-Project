from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(os.environ['DB_USER'], 
                                                                                os.environ['DB_PASSWORD'],
                                                                                os.environ['DB_HOST'],
                                                                                os.environ['DB_PORT'],
                                                                                os.environ['DB_NAME'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
Bootstrap(app)
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
"""
Customizing the login process
if a user attempte to access login_required without being logged in, it wil abort with a 401 error
when the login view is not set.

"""
login_manager.login_view = 'login'

"""
Login message
"""
login_manager.login_message = 'hmmm, login first!!'

from . import views