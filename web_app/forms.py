from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])
    rememberMe = BooleanField('rememberMe')




class SignupForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(max=50), Email('Enter a valid email address')])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])   



class MessageForm(FlaskForm):
    message = TextAreaField(validators=[InputRequired(), Length(max=140)])
    

class CommentForm(FlaskForm):
    comment = TextAreaField(validators=[InputRequired(), Length(max=140)])