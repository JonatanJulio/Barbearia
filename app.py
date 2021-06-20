from types import ClassMethodDescriptorType
from flask import Flask, render_template, abort, request
from repositories.todos_repository import TodosRepository
app = Flask(__name__)

from repositories.db import DB

#todos
#id: integer
#name: string
#status: string
#tasks:list<task>


#tasks
#id: integer
#todo_id: integer
#name: string
#description: string
#due_date: date:
#status: string

data = [
    {
        'id': 1,
        'name': 'CASA',
        'status': 'inactive',
        'tasks': [
            {
                'id': 1,
                'name': 'Lavar Pratos',
                'description': 'Os pratos estão todos sujos meu brother!',
                'due_date': '12/05/2021',
                'status': 'pending' 
            },
            {
                'id': 2,
                'name': 'Lavar Roupas',
                'description': 'Deixe de ser nojento!',
                'due_date': '12/05/2021',
                'status': 'delayed' 
            },
            {
                'id': 3,
                'name': 'Lavar Roupas',
                'description': 'Deixe de ser nojento!',
                'due_date': '12/05/2021',
                'status': 'completed' 
            }
        ]

    },
    {
        'id': 2,
        'name': 'Trabalho',
        'status': 'active',
        'tasks': [
            {
                'id': 3,
                'name': 'Imprimir documentação para contratação',
                'description': 'Falta imprimir CPF e comprovante de endereço',
                'due_date': '23/05/2021',
                'status': 'pending' 
            }
            
        ]

    }
]
#PostgreSQL

@app.route('/') # http://localhost:5000
def index():
    todos_repository = TodosRepository()
    todos = todos_repository.list()
    

    return render_template(
        'index.html',
        title = 'TODOs Uncisal',
        todos = todos
        
    )
# GET POST http://localhost:50000/todos/1
# GET http://localhost:50000/todos/1?nome=Tonho$idade=12
@app.route('/todos/<int:todo_id>', methods=['GET', 'POST'])
def todos(todo_id):
    todo = None

    for item in data:
            if item['id'] == todo_id:
                todo = item
                break
    
    if todo is None:
            abort(404)

    if request.method == 'POST':
        #name = request.form.get('name')
        #status = request.form.get('status')
        todo['name'] = request.form.get('name')
        todo['status'] = request.form.get('status')

    print(todo)    
    #else:
        #name = request.args.get('name')
        #password = request.args.get('password')
        #return f"{name} {password}"
    return render_template('todo.html', todo=todo)

@app.route('/sobre')
def sobre():
    return'Sistemas de TODO!'

#http://localhost:5000/contato/julio
@app.route('/contato/<nome>')
def contato(nome):
    return f"Nome do contato {nome}!"


