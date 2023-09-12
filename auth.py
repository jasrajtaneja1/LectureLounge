from flask import Blueprint, render_template, request, flash, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .models import User



auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('uvicEmailInput')
        password = request.form.get('passwordInput')

        user  = User.query.filter_by(email=email).first()
        if user:
            check_password_hash(user.password, password)
            flash('Logged in successfully!', category='success')
            login_user(user, remember = True)
            return redirect(url_for('views.ChatRooms'))
        else:
            flash('Incorrect password, try again', category='error')
    else:
        flash('Email does not exist!', category='error')

    return render_template("login.html",  user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup',  methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('uvicEmailInput')
        firstName = request.form.get('FirstNameInput')
        lastName = request.form.get('LastNameInput')
        password1 = request.form.get('passwordInput')
        password2 = request.form.get('passwordInput2')

        user  = User.query.filter_by(email=email).first()
        if user:
            flash('email already in use!', category='error')

        if len(firstName) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(lastName) <2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        
        elif password1!= password2:
            flash('Passwords do not match', category='error')
        elif len(password1) <8:
            flash('Password must be at least 8 characters', category='error')
        else:
            new_user = User(first_name = firstName, last_name = lastName, email = email, password = generate_password_hash(
                password1, method='sha256'))
            flash('Account succesfully created', category='success')
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.ChatRooms', user = current_user))

    




    return render_template("signup.html",  user=current_user)

 