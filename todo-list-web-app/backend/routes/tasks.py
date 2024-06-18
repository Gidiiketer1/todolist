from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from backend.models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        return create_task()

    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
@login_required
def update_or_delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'PUT':
        return update_task(task)
    elif request.method == 'DELETE':
        return delete_task(task)

def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    new_task = Task(title=title, description=description, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description})

def update_task(task):
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)

    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

def delete_task(task):
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

