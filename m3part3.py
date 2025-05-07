tasks = []

def add_task(task):
    if task in tasks:
        print("Task already exists.")
    else:
        tasks.append(task)
        print("Task added.")

def remove_task(task):
    if tasks in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("\nTasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")
    else:
        print("No tasks in the list.")

def todo_list():
    while True:
        print ("\n=======To-Do List Menu=======\n"
               "1. Add Task\n" 
               "2. Remove Task\n" 
               "3. View Tasks\n" 
               "4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Thank you for using To-Do List!")
            break
        else:
            print("Invalid input. Please try again.")

todo_list()