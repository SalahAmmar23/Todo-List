def add_task(todo_list):
    task = input("Enter A Task: ").lower()
    todo_list.append(task)
    print("Task Added.")
    
def view_tasks(todo_list):
    if not todo_list:
        print("There's no Tasks to review")
    else:
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    if not todo_list:
        print("There's nothing To remove ")
    else:
        task = input("Enter the Task Your Want to Remove: ").lower()
        if task in todo_list:
            todo_list.remove(task)
            print("Task Has been removed.")
        else:
            print("Task Not Found.")
 

todo_list = []
while True:
    ask_user = input("Enter the ToDolist command (Add, View, Remove, Exit): ").lower()
    if ask_user == "add":
        add_task(todo_list)
    elif ask_user == "view":
        view_tasks(todo_list)
    elif ask_user == "remove":
        remove_task(todo_list)
    elif ask_user == "exit":
        break
    else:
        print("Invalid command")