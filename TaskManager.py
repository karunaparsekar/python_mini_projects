import os

def main():
    '''main menu to interact'''
    while True:
        print("\nTask Manager")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Delete Task")
        print("4.Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task:")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            delete_task_number = int(input("Enter task number tha you want to delete: "))
            delete_task(delete_task_number)

        elif choice == "4":
            print("Exiting Task Manager")
            break;
        else:
            print("Invalid choice. Please enter a valid option")

Task_File = "tasks.txt"

def add_task(task):
    """adds task to the file"""
    with open(Task_File, "a") as file:
        file.write(task + "\n")
        print(f"Task {task} added successfully!")


def view_tasks():
    "views all tasks from the file"

    if not os.path.exists(Task_File) or os.stat(Task_File).st_size == 0:
        print("No tasks available")
        return

    with open(Task_File, "r") as file:
        tasks = file.readlines()

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start = 1):
        print(f"{index} : {task}")

def delete_task(delete_task_number):
    "delete specified task from the list"
    if not os.path.exists(Task_File) or os.stat(Task_File).st_size == 0:
        print("No tasks to delete")
        return

    with open(Task_File, "r") as file:
        tasks = file.readlines()

    if delete_task_number < 1 or delete_task_number > len(tasks):
        print("invalid task number")
        return

    del tasks[delete_task_number - 1]

    with open(Task_File, "w") as file :
        file.writelines(tasks)

    print(f"task {delete_task_number} deleted successfully")




if __name__ == "__main__":
    main()