def task():
    print("Welcome to my to-do-list program!")
    tasks= []

    total_task= int(input("Enter number of tasks you want to add:"))
    for i in range(1, total_task+1):
        task_name= input(f"Enter task no. {i}:")
        tasks.append(task_name)

    print(f"Todays tasks are:\n{tasks}")

    while True:
        choice_menu= int(input("Enter:\n 1-Add\n 2-View\n 3-Delete\n 4-Update\n 5-Mark done\n 6-Exit"))
        
        if choice_menu== 1:
            add=input("Enter the task you want to add:")
            tasks.append(add)
            print(f"Task {add} has been successfully added!")

        elif choice_menu== 2:
            view= list(tasks)
            print(view)

        elif choice_menu== 3:
            del_task= input("Enter task you want to delete:")
            if del_task in tasks:
                index_no= tasks.index(del_task)
                del tasks[index_no]
                print(f"Task {del_task} has been deleted!")
            else:
                print("Entered task is not in the list!")
        
        elif choice_menu== 4:
            update_task= input("Enter task you want to update:")
            if update_task in tasks:
                update_by= input("Enter new task:")
                index_no= tasks.index(update_task)
                tasks[index_no]= update_by
                print("Your task has been updated!")               
            else:
                print("Entered task is not in the list for updating!")

        elif choice_menu== 5:
            mark_task= input("Enter task you want to mark as done:")
            if mark_task in tasks:
                tasks.remove(mark_task)
                print("Task is completed and removed from the list!")
            else:
                print("Entered task is not in the list!")

        elif choice_menu== 6:
            break

        else:
            print("Invalid operations!!")
                
task()


