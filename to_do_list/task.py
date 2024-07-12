# task.py

import json
from datetime import datetime

class Task:
    _id_counter = 1

    def __init__(self, title, description, due_date=None, priority="Low", completed=False):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(task_dict):
        task = Task(
            title=task_dict["title"],
            description=task_dict["description"],
            due_date=task_dict["due_date"],
            priority=task_dict["priority"],
            completed=task_dict["completed"]
        )
        task.id = task_dict["id"]
        task.created_at = task_dict["created_at"]
        Task._id_counter = max(Task._id_counter, task.id + 1)
        return task
