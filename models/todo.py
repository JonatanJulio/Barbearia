
from repositories.tasks_repository import TasksRepository
from shared.models import db



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')
    tasks = db.relationship('Task', backref='todo', lazy=True)

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self) -> str:
        return f"<Todo {self.name}>"

    


#class Todo:
#    def __init__(self, id, name, status):
#        self.id = id
#        self.name = name 
#        self.status = status
#        self.tasks = []
#        self.tasks_repository = TasksRepository()


#    def get_tasks(self):
#        if len(self.tasks) == 0:
#            self.tasks = self.tasks_repository.list_by_todo_id(self.id)

#        return self.tasks