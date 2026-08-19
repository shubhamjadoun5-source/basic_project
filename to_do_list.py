tasks=[]

def add_task():
    task= input("Enter Task: ")
    tasks.append(task)
    print("Task Added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else: 
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i])

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    num =  int(input("Enter task number to delete: "))
    if num>0 and num<= len(tasks):
        removed=tasks.pop(num-1)
        print("Removed: ", removed)
    else:
        print("Invalid task Number")


while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice, try again")
