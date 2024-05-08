task_list = []

ask_user = input("Enter the ToDolist command (Add, View, Remove, Exit) : ").lower()

while(True):
    if ask_user.lower() == "add" :
        task = input("Enter a Task: ").lower()
        task_list.append(task)
        print("Task Has Been Added. ")
        
    