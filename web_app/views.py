from . import app, db, bcrypt
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, SignupForm
from .models import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user_by(form.username.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                return redirect(url_for('dashboard'))
    flash('Invalid login info')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hash_pwd)
        new_user.save()
        return redirect(url_for('dashboard'))
    return render_template('signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')