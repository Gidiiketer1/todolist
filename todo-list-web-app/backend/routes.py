from flask import request, jsonify, Blueprint, render_template, redirect, url_for, flash
from .models import db, User, Task
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('main', __name__)

@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'register':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            if not username or not email or not password:
                flash('Missing required fields', 'danger')
                return redirect(url_for('main.auth'))
            if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
                flash('User already exists', 'danger')
                return redirect(url_for('main.auth'))
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('User registered successfully', 'success')
            return redirect(url_for('main.auth'))
        elif action == 'login':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Logged in successfully', 'success')
                return redirect(url_for('main.profile'))
            else:
                flash('Invalid credentials', 'danger')
                return redirect(url_for('main.auth'))
    return render_template('auth.html')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@bp.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        data = request.get_json()
        new_task = Task(title=data['title'], description=data['description'], user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task added successfully"}), 201
    else:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('tasks.html', tasks=tasks)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('main.index'))
