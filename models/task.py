from shared.models import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='active')
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return f"<Task {self.name}>"

#class Task:
#    def __init__(self, id, todo_id, name, description, due_date, status):
#        self.id = id 
#        self.todo_id = todo_id 
#        self.name = name
#        self.description = description 
#        self.due_date = due_date
#        self.status = status