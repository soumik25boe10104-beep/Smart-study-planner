import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    name = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")
    task = {"name": name, "priority": priority, "done": False}
    tasks.append(task)
    save_tasks(tasks)

def view_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i+1}. {task['name']} [{task['priority']}] - {status}")

def complete_task(tasks):
    view_tasks(tasks)
    i = int(input("Enter task number: ")) - 1
    tasks[i]["done"] = True
    save_tasks(tasks)

def delete_task(tasks):
    view_tasks(tasks)
    i = int(input("Enter task number to delete: ")) - 1
    tasks.pop(i)
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1.Add 2.View 3.Complete 4.Delete 5.Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break

main()