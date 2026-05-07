tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        tasks.pop(task_num - 1)
        print("Task Removed!")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid Choice")