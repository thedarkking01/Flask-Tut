# app/todo/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Task
from .. import db

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@todo_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    t = Task(content=request.form['task'].strip(), user_id=current_user.id)
    db.session.add(t); db.session.commit()
    return redirect(url_for('todo.index'))

@todo_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    t = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(t); db.session.commit()
    return redirect(url_for('todo.index'))

@todo_bp.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_task(id):
    t = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        t.content = request.form['task'].strip()
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('edit.html', task=t)
