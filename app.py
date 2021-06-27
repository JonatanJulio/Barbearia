from types import ClassMethodDescriptorType

from flask import Flask, abort, session, flash, render_template, request, redirect, url_for, \
    make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate


from shared.models import db
from models.todo import Todo
from models.task import Task

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/todolist"
db.init_app(app)
migrate = Migrate(app, db)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/') # http://localhost:5000
def index():
    # redireciona para o login se não estiver logado
    if 'username' not in session:
        return redirect(url_for('login'))
    
    todos = Todo.query.all()
    
    response = make_response(
        render_template(    
            'index.html',
            title = 'TODOs Uncisal',
            todos = todos
        )
    )
    # response.set_cookie('language', 'pt-BR')

    return response

@app.route('/set_language/<language>')
def set_language(language):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('language', language)
    
    return response

@app.route('/todos/<int:todo_id>', methods=['GET', 'POST'])
def todos(todo_id):
    language = request.cookies.get('language')

    todo = Todo.query.get_or_404(todo_id)
    
    if request.method == 'POST':
        todo.name = request.form.get('name')
        todo.status = request.form.get('status')
        db.session.add(todo)
        db.session.commit()

    return render_template('todo.html', todo=todo, language=language)

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

#### LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'Jonatan' and password == '123':
            session['username'] = username
            flash('Usuário autenticado com sucesso.', 'info')
            return redirect(url_for('index'))
        else:
            # abort(403)
            flash('Nome de usuário e/ou senha incorreto(s)', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/api/todos')
def api_todos():
    todos = Todo.query.all()

    todo_list = []
    for todo in todos:
        todo_list.append(
            {
                "id": todo.id,
                "name": todo.name,
                "status": todo.status

            }
        )

    return jsonify(todo_list)

    # return [{"id": todo['id'], "name": todo["name"]} for todo in todos] 
    
