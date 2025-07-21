def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task[1] else "✖"
            print(f"{i}. [{status}] {task[0]}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append([title, False])
    print("Task added.")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1][1] = True
            print("Task marked as completed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            tasks.pop(index - 1)
            print("Task deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    tasks = []
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Corrected line:
if __name__ == "__main__":
    main()
