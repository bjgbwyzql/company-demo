tasks = []

def greet():
    print("Welcome to Todo App!")

def add_task(text):
    tasks.append({"text": text, "done": False})
    print(f"Added: {text}")


def list_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {i}. {task['text']}")


def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Completed: {tasks[index - 1]['text']}")
    else:
        print("Invalid task number")

