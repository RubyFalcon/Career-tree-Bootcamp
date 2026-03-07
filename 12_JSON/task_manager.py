import json
import os
from app import Task

class TaskManager:
    """Manages a collection of tasks with JSON persistence"""
    DATA_FILE = "tasks.json"

    def __init__(self):
        self.tasks: list[Task] = []
        self.load() #Load from disk on startup

    # CRUD = Create, Read, Update, Delete
    def add_tasks(self, title, priority="Low")-> Task:
        task = Task(title, priority)
        self.tasks.append(task)
        self.save() 


    def get_task(self, task_id:int)-> Task | None:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def complete_task(self,task_id:int)-> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            # self.save()
            return True
        return False

    def delete_tasks(self,task_id:int)-> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    def list_tasks(self, show_done=True)-> list[Task]:
        if show_done:
            return self.tasks
        result = []
        for t in self.tasks:
             if not t.done:
                result.append(t)
        return result
    
    def save(self):
        """Save all tasks to the JSON File"""
        task_list = []
        done_count = 0
        for t in self.tasks:
            task_list.append(t.to_dict())
            if t.done:
                done_count += 1
        data = {
            "tasks":task_list ,
            "meta": {
                "total": len(self.tasks),
                "done": done_count,
            }
            
            
        }
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not os.path.exists(self.DATA_FILE):
            return
        try:
            with open(self.DATA_FILE,"r") as f:
                data = json.load(f)
            self.tasks = []
            task_list = data.get('tasks',[])
            for d in task_list:
                task = Task.from_dict(d)
                self.tasks.append(task)
        except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
            print(f"Warning: could not load data file: {e}")

task_app = TaskManager()
task_app.add_tasks("Shopping")
print(task_app.get_task(1))
task_app.add_tasks("Grab a meal")
print(task_app.get_task(2))
