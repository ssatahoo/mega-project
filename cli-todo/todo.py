import json
import sys
import os

DB_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['name']}")

def add_task(tasks, name):
    tasks.append({"name": name, "done": False})
    print(f"Added task: {name}")

def mark_done(tasks, task_id):
    try:
        tasks[task_id]["done"] = True
        print(f"Marked task {task_id+1} as done.")
    except IndexError:
        print("Invalid task ID.")

def delete_task(tasks, task_id):
    try:
        removed = tasks.pop(task_id)
        print(f"Deleted task: {removed['name']}")
    except IndexError:
        print("Invalid task ID.")

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python todo.py [add|list|done|delete] [task]")
        return

    command = args[0]
    tasks = load_tasks()

    if command == "add" and len(args) >= 2:
        task_name = " ".join(args[1:])
        add_task(tasks, task_name)
    elif command == "list":
        list_tasks(tasks)
    elif command == "done" and len(args) == 2:
        mark_done(tasks, int(args[1]) - 1)
    elif command == "delete" and len(args) == 2:
        delete_task(tasks, int(args[1]) - 1)
    else:
        print("Invalid command or arguments.")

    save_tasks(tasks)

if __name__ == "__main__":
    main()

