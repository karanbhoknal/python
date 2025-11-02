import json
import os

# ------------------------
# Task Class
# ------------------------
class Task:
    def __init__(self, title, description):
        """
        Initialize a Task object
        :param title: Title of the task
        :param description: Description of the task
        """
        self.title = title
        self.description = description
        self.completed = False  # Task is incomplete by default


# ------------------------
# TaskManager Class
# ------------------------
class TaskManager:
    def __init__(self, filename="tasks.json"):
        """
        Initialize TaskManager
        :param filename: JSON file to store tasks
        """
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from the JSON file
        :return: List of Task objects
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    # Convert dictionaries from JSON into Task objects
                    return [Task(**task) for task in data]
            except json.JSONDecodeError:
                # Return empty list if file is empty or corrupted
                return []
        else:
            return []

    def save_tasks(self):
        """
        Save current tasks list to JSON file
        """
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_task(self, title, description):
        """
        Add a new task
        :param title: Title of the task
        :param description: Description of the task
        """
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def delete_task(self, task_number):
        """
        Delete a task by its number
        :param task_number: 1-based index of the task
        """
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Deleted task: {removed_task.title}")
        else:
            print("Invalid task number!")

    def mark_complete(self, task_number):
        """
        Mark a task as complete
        :param task_number: 1-based index of the task
        """
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            self.save_tasks()
            print(f"Task '{self.tasks[task_number - 1].title}' marked as complete!")
        else:
            print("Invalid task number!")

    def view_tasks(self):
        """
        Display all tasks with status
        """
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\nYour Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔️ Completed" if task.completed else "❌ Incomplete"
            print(f"{idx}. {task.title} - {task.description} [{status}]")


# ------------------------
# Main Menu
# ------------------------
def main():
    """
    Main function to run the To-Do List Manager
    """
    manager = TaskManager()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == "3":
            manager.view_tasks()
            try:
                task_no = int(input("Enter task number to delete: "))
                manager.delete_task(task_no)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            manager.view_tasks()
            try:
                task_no = int(input("Enter task number to mark complete: "))
                manager.mark_complete(task_no)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# ------------------------
# Run Program
# ------------------------
if __name__ == "__main__":
    main()
