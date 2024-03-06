import uuid
import cmd
import argparse

# Group 6922

class Task:
    def __init__(self, title, desc):
        self.id = str(uuid.uuid4())
        self.title = title
        self.desc = desc
        self.isCompleted = False

    def __str__(self):
        return f"{self.id}:{self.title} {self.desc} {self.isCompleted}"

    def mark_as_completed(self):
        self.isCompleted = True

        
class TaskManager:
    def __init__(self, tasks = {}):
        self.tasks = tasks
        
    def add_task(self, title, desc):
        task = Task(title, desc)
        self.tasks[task.id] = task
        
        
    def remove_task(self, id):
        try:
            del self.tasks[id]
        except KeyError:
            print("Tasks not found")
    
    def mark_task_completed(self,id):
        if self.tasks[id] is not None:
            self.tasks[id].mark_as_completed()
    
    def __str__(self):
        return f"{self.id}:{self.title} {self.desc} {self.isCompleted}"

    def list_tasks(self):
        for k,v in self.tasks.items():
            print(f"{v}")

    def find_task(self,id):
        if self.tasks[id] is not None:
            return(self.tasks[id])
        else:
            return(None)

 
class CLI(cmd.Cmd):
    a = TaskManager()
    
    def do_add(self, arg):
        parser = argparse.ArgumentParser(description="Task Manager CLI")
        parser.add_argument("--title", help="Title of the task")
        parser.add_argument("--desc", help="Description of the task")
        args = parser.parse_args(arg.split())
        x = CLI.a.add_task(args.title, args.desc)
        CLI.a.list_tasks()

    def  do_get_all(self, arg):
        CLI.a.list_tasks()

    def do_complete(self, arg):
        parser = argparse.ArgumentParser(description="Task Manager CLI")
        parser.add_argument("--id", help="Id of the task")
        args = parser.parse_args(arg.split())
        CLI.a.mark_task_completed(args.id)

    def do_remove(self, arg):
        parser = argparse.ArgumentParser(description="Task Manager CLI")
        parser.add_argument("--id", help="Id of the task")
        args = parser.parse_args(arg.split())
        CLI.a.remove_task(args.id)


if __name__ == '__main__':
    CLI().cmdloop()
