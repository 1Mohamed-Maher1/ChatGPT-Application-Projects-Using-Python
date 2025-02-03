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


if __name__ == "__main__":
    app = TodoApp()
    app.start()
