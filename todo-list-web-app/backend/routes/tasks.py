from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from backend.models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        return handle_task_creation()

    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

def handle_task_creation():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], user_id=current_user.id)

    db.session.add(new_task)
    db.session.commit()

    # Redirect to the tasks page after adding a new task
    return redirect(url_for('tasks.tasks'))
