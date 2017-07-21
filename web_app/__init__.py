from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
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



from . import views