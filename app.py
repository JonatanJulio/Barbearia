from types import ClassMethodDescriptorType

from flask import Flask, abort, render_template, request, redirect, url_for
from flask_migrate import Migrate


from shared.models import db
from models.todo import Todo
from models.task import Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/todolist"
db.init_app(app)
migrate = Migrate(app, db)



@app.route('/') # http://localhost:5000
def index():
    todos = Todo.query.all()
    
    


    return render_template(
        'index.html',
        title = 'TODOs Uncisal',
        todos = todos
        
    )

@app.route('/todos/<int:todo_id>', methods=['GET', 'POST'])
def todos(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    
    if request.method == 'POST':
        todo.name = request.form.get('name')
        todo.status = request.form.get('status')
        db.session.add(todo)
        db.session.commit()

    return render_template('todo.html', todo=todo)

@app.route('/todos', methods=['POST'])
def create_todo():
    name = request.form.get('name')
    status = request.form.get('status')

    todo = Todo(name=name, status=status)

    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todos',todo_id=todo.id))

@app.route('/todos/<int:todo_id>/delete', methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/sobre')
def sobre():
    return'Sistemas de TODO!'

#http://localhost:5000/contato/julio
@app.route('/contato/<nome>')
def contato(nome):
    return f"Nome do contato {nome}!"


