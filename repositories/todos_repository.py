from repositories.base_repository import BaseRepository
from models.todo import Todo
from repositories.db import DB


class TodosRepository(BaseRepository):
    def list(self):
        result = self.execute(
            'SELECT id, name, status FROM todos ORDER BY id desc'
        )
        todos = []

        for row in result:
            todo = Todo(id=row[0], name=row[1], status=row[2])
            todos.append(todo) 
            
        
        return todos