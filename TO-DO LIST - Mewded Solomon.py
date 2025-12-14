tasks = []
completed_tasks = []
def display_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]['name']}")
    print()


def add_task():
    name = input("Enter new task: ")
    tasks.append({"name": name, "completed": False})


def remove_task():
    display_tasks()
    if len(tasks) == 0:
        print("There isn't any to Remove!!")
        return
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task removed!")
    else:
        print("INVALID TASK NUMBER TO REMOVE")


def edit_task():
    display_tasks()
    if len(tasks) == 0:
        return
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        new_name = input("Enter new task name: ")
        tasks[index]["name"] = new_name
        print("Task updated!")
    else:
        print("INVALID NUMBER TO EDIT!!")


def complete_task():
    display_tasks()
    if len(tasks) == 0:
        return
   
    index = int(input("Enter task number to mark complete: ")) - 1
   
    if 0 <= index < len(tasks):
        completed_task = tasks.pop(index)
        completed_task["completed"] = True  
        completed_tasks.append(completed_task)  
       
        print("Task marked as completed and moved to completed tasks!")
    else:
        print("INVALID NUMBER!!!!!!")
def show_completed_tasks():
    if len(completed_tasks) == 0:
        print("NO COMPLTETED TASKS YET.1")
    else:
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task['name']}")
        print()


def main():
    print("========== TO-DO LIST ==========")
    while True:
        display_tasks()
        print("MENU")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Mark Task Complete")
        print("5. View Completed Tasks")
        print("6. Exit")                  
       
        choice = input("Choose an option (1-6): ")
       
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":  
            show_completed_tasks()
        elif choice == "6":  
            print("today's task summary")
            if len(completed_tasks) == 0 and len(tasks) == 0:  
                print("you had no task today")
                print("Exiting pending...")
            else:
                print(f"You completed {len(completed_tasks)} tasks.")
                print(f"You have {len(tasks)} tasks left.")
                print("That's it for today")
                print("Exiting pending.......")
            break
        else:
            print("ERROR, Try again")
main()

tasks = []
completed_tasks = []
def display_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]['name']}")
    print()


def add_task():
    name = input("Enter new task: ")
    tasks.append({"name": name, "completed": False})


def remove_task():
    display_tasks()
    if len(tasks) == 0:
        print("There isn't any to Remove!!")
        return
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task removed!")
    else:
        print("INVALID TASK NUMBER TO REMOVE")


def edit_task():
    display_tasks()
    if len(tasks) == 0:
        return
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        new_name = input("Enter new task name: ")
        tasks[index]["name"] = new_name
        print("Task updated!")
    else:
        print("INVALID NUMBER TO EDIT!!")


def complete_task():
    display_tasks()
    if len(tasks) == 0:
        return
   
    index = int(input("Enter task number to mark complete: ")) - 1
   
    if 0 <= index < len(tasks):
        completed_task = tasks.pop(index)
        completed_task["completed"] = True  
        completed_tasks.append(completed_task)  
       
        print("Task marked as completed and moved to completed tasks!")
    else:
        print("INVALID NUMBER!!!!!!")
def show_completed_tasks():
    if len(completed_tasks) == 0:
        print("NO COMPLTETED TASKS YET.1")
    else:
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task['name']}")
        print()


def main():
    print("========== TO-DO LIST ==========")
    while True:
        display_tasks()
        print("MENU")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Mark Task Complete")
        print("5. View Completed Tasks")
        print("6. Exit")                  
       
        choice = input("Choose an option (1-6): ")
       
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":  
            show_completed_tasks()
        elif choice == "6":  
            print("today's task summary")
            if len(completed_tasks) == 0 and len(tasks) == 0:  
                print("you had no task today")
                print("Exiting pending...")
            else:
                print(f"You completed {len(completed_tasks)} tasks.")
                print(f"You have {len(tasks)} tasks left.")
                print("That's it for today")
                print("Exiting pending.......")
            break
        else:
            print("ERROR, Try again")
main()

