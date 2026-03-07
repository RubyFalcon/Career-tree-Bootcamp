# JSON - Javascipt Object Notation
# JSON - Text format for storing structured data, like Python Dicts
# JSON - supports strings, boolean, nulls, arrays[]. lists, and objects[].
# Serialisation --> Deserialisation
# Convert objects to dicts(serilalize) and back (de-serialize)

import json

class Task:
    count = 1
    def __init__(self, title,priority="low"):
        self.task_id = Task.count
        self.title = title
        self.priority = priority
        self.done = False
        self.tags = []
        Task.count += 1
    def __str__(self):
        return str(self.to_dict())
    
    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', priority='{self.priority}', done={self.done})"
    
    def complete(self):
        self.done = True

    # Serialisation
    def to_dict(self)-> dict:
        """Convert this task into a JSON dictionary"""
        return {
            "id": self.task_id,
            "title":self.title,
            "priority" : self.priority,
            "done": self.done,
            "tags": self.tags,
            "type": self.__class__.__name__
        }
    # Deserialization
    @classmethod
    def from_dict(cls, data:dict)-> "Task":
        """Create a task from a dictionary"""
        task = cls(data['title'],data.get("priority", "low"))
        task.done = data.get("done", False)
        task.tags = data.get("tags", [])
        Task.count = max(Task.count, task.task_id+ 1)
        return task
    
    
# task1 = Task("Get Food","medium")
# task1.tags = ["Bananas","Oranges"]
# task_dict = task1.to_dict()

# task2 = Task.from_dict(task_dict)
# print(task2.title)
# print(task2.task_id)

# task_json:json = json.dumps(task_dict)
# print(f"Our json task is  :\n {task_dict}")