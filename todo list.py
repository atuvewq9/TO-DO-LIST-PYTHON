
# Online Python - IDE, Editor, Compiler, Interpreter
tasks = []

while True:

    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    # ADD TASK
    if choice == "1":

        task = input("Enter task: ")
        tasks.append(task)

        print("Task added!")

    # VIEW TASKS
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(i, task)

    # DELETE TASK
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

            num = int(input("Enter task number to delete: "))

            if num >= 1 and num <= len(tasks):

                removed = tasks.pop(num - 1)

                print(removed, "deleted!")

            else:
                print("Invalid task number.")

    # EXIT
    elif choice == "4":

        print("Goodbye!")
        break

    else:
        print("Invalid choice.")