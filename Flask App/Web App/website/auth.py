from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        user = User.query.filter_by(email=email).first()
        if user:
            if (check_password_hash(user.password, password)) & (user.role == 'User'): ## why doesnt this work?
                flash('Logged in successfully!', category='success')
                login_user(user)
                return redirect(url_for('views.your_thoughts'))
            elif (check_password_hash(user.password, password)) & (user.role == 'Specialist'):
                flash('Logged in successfully!', category='success')
                login_user(user)
                return redirect(url_for('views.your_patients'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')
        accepted_roles= ['User', 'Specialist']
        print(role)
        print('test role')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif role not in accepted_roles:
            flash('You must choose either User or Specialist', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 3 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name,role = role, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            if role == 'User':
                login_user(new_user)
                flash('Account created!', category='success')
                return redirect(url_for('views.your_thoughts'))
            elif role == 'Specialist':
                login_user(new_user)
                flash('Account created!', category='success')
                return redirect(url_for('views.your_patients'))

    return render_template("sign_up.html", user=current_user)
    
