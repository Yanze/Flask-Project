from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])
    rememberMe = BooleanField('rememberMe')




class SignupForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(max=50), Email('Enter a valid email address')])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])   



# class MessageForm(FlaskForm):
#     message = StringField('message', validators=[InputRequired(), Length(max=500)])
#     user
