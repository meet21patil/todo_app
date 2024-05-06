class Task:
    def __init__(self, unique_id, description, completed=False):
        self.unique_id = unique_id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task ID: {self.unique_id}\nDescription: {self.description}\nStatus: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully!")

    def delete_task(self, identifier):
        deleted = False
        for task in self.tasks:
            if str(task.unique_id) == identifier or task.description.lower() == identifier.lower():
                self.tasks.remove(task)
                deleted = True
                print("Task deleted successfully!")
                break
        if not deleted:
            print("Task not found.")

    def mark_task_as_completed(self, identifier):
        marked = False
        for task in self.tasks:
            if str(task.unique_id) == identifier or task.description.lower() == identifier.lower():
                task.completed = True
                marked = True
                print("Task marked as completed!")
                break
        if not marked:
            print("Task not found.")

    def display_tasks(self):
        if self.tasks:
            print("Current Tasks:")
            for task in self.tasks:
                print(task)
                print("-" * 20)
        else:
            print("No tasks in the to-do list.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display To-Do List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip().lower()

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            identifier = input("Enter task ID or description to delete: ")
            todo_list.delete_task(identifier)
        elif choice == "3":
            identifier = input("Enter task ID or description to mark as completed: ")
            todo_list.mark_task_as_completed(identifier)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
