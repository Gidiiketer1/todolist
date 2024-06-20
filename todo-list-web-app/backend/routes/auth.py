from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from backend import db
from backend.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'login':
            return handle_login()
        elif action == 'register':
            return handle_registration()
    
    return render_template('auth.html')

def handle_login():
    email = request.form['email']
    password = request.form['password']
    
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        login_user(user)
        # Redirect to the tasks page after login
        return redirect(url_for('tasks.tasks'))
    else:
        flash('Invalid email or password', 'error')
        return redirect(url_for('auth.auth'))

def handle_registration():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        flash('Username or email already exists', 'error')
        return redirect(url_for('auth.auth'))

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    # Redirect to the tasks page after registration
    return redirect(url_for('tasks.tasks'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.auth'))