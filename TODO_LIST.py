task_list = []

while(True):
    ask_user = input("Enter the ToDolist command (Add, View, Remove, Exit) : ").lower()
    if ask_user.lower() == "add" :
        task = input("Enter a Task: ").lower()
        task_list.append(task)
        print("Task Has Been Added. ")
    elif ask_user.lower() == "view":
        if task_list == []:     # if the task_list is empty we want to stop cuz there's no lists
            print("There's no tasks To review.")
            break
        else:
             for task in task_list:
                 print(task)
    elif ask_user.lower() == "remove":
        if not task_list:
            print("No tasks found to remove.")
        else:
            task = input("Enter the Task you want to remove : ").lower()
            if task in task_list:
                task_list.remove(task)
                print("Task Has been removed.")
            else:
                print("Task Not Found.")
    elif ask_user == "exit":
        break
    else:
        print("invalid command")    
        
        
    