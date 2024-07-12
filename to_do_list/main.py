# main.py

import json
from task import Task

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks_dict = json.load(file)
            return [Task.from_dict(task) for task in tasks_dict]
    except FileNotFoundError:
        return []

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete/Incomplete")
    print("6. Search Tasks")
    print("7. Save and Exit")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    priority = input("Enter task priority (Low, Medium, High): ")
    tasks.append(Task(title, description, due_date, priority))
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    tasks = sorted(tasks, key=lambda x: (x.priority, x.due_date))
    for task in tasks:
        status = "Completed" if task.completed else "Incomplete"
        print(f"[{task.id}] {task.title} - {task.description} (Due: {task.due_date}, Priority: {task.priority}) [{status}]")

def update_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task ID to update: "))
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        task.title = input(f"Enter new title (current: {task.title}): ")
        task.description = input(f"Enter new description (current: {task.description}): ")
        task.due_date = input(f"Enter new due date (current: {task.due_date}): ")
        task.priority = input(f"Enter new priority (current: {task.priority}): ")
        print("Task updated successfully.")
    else:
        print("Task not found.")

def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task ID to delete: "))
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        tasks.remove(task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def mark_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task ID to mark as complete/incomplete: "))
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        task.completed = not task.completed
        status = "Completed" if task.completed else "Incomplete"
        print(f"Task marked as {status}.")
    else:
        print("Task not found.")

def search_tasks(tasks):
    keyword = input("Enter keyword to search for: ")
    results = [task for task in tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
    if results:
        for task in results:
            status = "Completed" if task.completed else "Incomplete"
            print(f"[{task.id}] {task.title} - {task.description} (Due: {task.due_date}, Priority: {task.priority}) [{status}]")
    else:
        print("No tasks found matching the keyword.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task(tasks)
        elif choice == '6':
            search_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
