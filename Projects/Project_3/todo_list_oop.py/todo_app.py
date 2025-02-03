# todo_app.py

from todo_list import TodoList

class TodoApp:
    """
    This class manages user interactions with the TodoList.
    """
    def __init__(self):
        self.todo_list = TodoList()

    def start(self):
        """
        Starts the main loop for user interaction.
        """
        while True:
            user_action = input("Enter a command (add, view, remove, exit): ").strip().lower()
            if user_action == "add":
                task = input("Enter a task: ")
                self.todo_list.add_task(task)
            elif user_action == "view":
                self.todo_list.view_tasks()
            elif user_action == "remove":
                task = input("Enter a task to remove: ")
                self.todo_list.remove_task(task)
            elif user_action == "exit":
                break
            else:
                print("Invalid command")
