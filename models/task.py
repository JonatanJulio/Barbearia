class Task:
    def __init__(self, id, todo_id, name, description, due_date, status):
        self.id = id 
        self.todo_id = todo_id 
        self.name = name
        self.description = description 
        self.due_date = due_date
        self.status = status