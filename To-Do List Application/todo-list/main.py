# To-Do List Application

tasks = []

def add_task():
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added successfully!")

def mark_task_completed():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['description']} {'[Completed]' if task['completed'] else ''}")

    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[task_index]["completed"] = True
    print("Task marked as completed.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['description']} {'[Completed]' if task['completed'] else ''}")

# Main application loop
while True:
    print("======= TO-DO LIST =======")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_completed()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
