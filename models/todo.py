
from repositories.tasks_repository import TasksRepository
class Todo:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name 
        self.status = status
        self.tasks = []
        self.tasks_repository = TasksRepository()


    def get_tasks(self):
        if len(self.tasks) == 0:
            self.tasks = self.tasks_repository.list_by_todo_id(self.id)

        return self.tasks