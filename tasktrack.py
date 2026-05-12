tasktrack.py

Simple Task Tracker Application

import json import os

TASKS_FILE = "tasks.json"

def load_tasks(): if os.path.exists(TASKS_FILE): with open(TASKS_FILE, "r") as file: return json.load(file) return []

def save_tasks(tasks): with open(TASKS_FILE, "w") as file: json.dump(tasks, file, indent=4)

def add_task(tasks): task = input("Enter new task: ") tasks.append({"task": task, "done": False}) save_tasks(tasks) print("Task added successfully!\n")

def view_tasks(tasks): if not tasks: print("No tasks found.\n") return

print("\nYour Tasks:")
for i, task in enumerate(tasks, start=1):
    status = "✔" if task["done"] else "✘"
    print(f"{i}. {task['task']} [{status}]")
print()

def complete_task(tasks): view_tasks(tasks)

try:
    task_no = int(input("Enter task number to mark complete: "))
    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    else:
        print("Invalid task number.\n")
except ValueError:
    print("Please enter a valid number.\n")

def delete_task(tasks): view_tasks(tasks)

try:
    task_no = int(input("Enter task number to delete: "))
    if 1 <= task_no <= len(tasks):
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['task']}\n")
    else:
        print("Invalid task number.\n")
except ValueError:
    print("Please enter a valid number.\n")

def main(): tasks = load_tasks()

while True:
    print("==== Task Tracker ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Exiting Task Tracker...")
        break
    else:
        print("Invalid choice. Please try again.\n")

if name == "main": main()
