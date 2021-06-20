from models.task import Task
from repositories.db import DB
from repositories.base_repository import BaseRepository


class TasksRepository(BaseRepository):
    def list_by_todo_id(self, todo_id):
        result = self.execute(
            f"SELECT id, todo_id, name, description, due_date, status FROM tasks WHERE todo_id = {todo_id} ORDER BY id desc"
        )
        tasks = []

        for row in result:
            task = Task(
                id=row[0],
                todo_id=row[1],
                name=row[2],
                description=row[3],
                due_date=row[4], 
                status=row[5]
            )
            tasks.append(task)
            
        return tasks