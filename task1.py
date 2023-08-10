to_do_list = []
while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        to_do_list.append({'task': task, 'done': False})
        print("Task added!")

    elif choice == '2':
        print("Tasks:")
        for index, task in enumerate(to_do_list, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

    elif choice == '3':
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(to_do_list):
            to_do_list[task_index]['done'] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
