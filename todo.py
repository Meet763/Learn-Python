import json

def display_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Save and exit")

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "\u2713" if task['completed'] else "\u2717"
        print(f"{index}. {task['task']} [{status}]")

def add_task(tasks):
    task_description = input("\nEnter a new task: ")
    tasks.append({"task": task_description, "completed": False})
    print(f"Task '{task_description}' added.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
