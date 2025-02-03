# todo_list.py

class TodoList:
    """
    This class manages the to-do list by providing methods to add, view, and remove tasks.
    """
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        """
        Adds a task to the to-do list.
        """
        self.todo_list.append(task)
        print("Task added.")

    def view_tasks(self):
        """
        Displays all tasks in the to-do list.
        """
        if not self.todo_list:
            print("No tasks to display.")
        else:
            for task in self.todo_list:
                print(task)

    def remove_task(self, task):
        """
        Removes a specified task from the to-do list.
        """
        if task in self.todo_list:
            self.todo_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
