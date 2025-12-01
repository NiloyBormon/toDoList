import json
import time
import requests

# version = "0.0.1"
# def update(version):
#     currentVersion = requests.get("https://raw.githubusercontent.com/NiloyBormon/UpdateCheck/refs/heads/main/Version").text
#     if version != currentVersion:
#         print("Trying to download the latest version!")
#         # with open("")


print("Hello! Welcome to my todolist app!")
tasks = {}
try:              
    with open("data.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    with open("data.json","w") as f:
        json.dump(tasks,f)

while True:
    action = input("What are u trying to do? \n1: Create a new task.\n2: View specific task.\n3: View all tasks. \n4: delet a specific task.\n5: delet all tasks.\nEnter (1-5): ")
    if action == "1":
        while True:
            key = input("Enter task number: ")
            if (key in tasks):
                print("Task number alredy exist! Try another.")
                continue
            elif key == "" :
                print("You need to enter a task number or task letter")
                continue
            else :
                break

        value = input("Enter task description: ")
        tasks[key] = value

        with open("data.json","w") as f:
            json.dump(tasks,f)
        print(f"your no {key} task saved as \"{tasks[key]}\"")
        input()

    elif action == "2":
        while True:
            key = input("Enter which task u want to view: ")
            if key in tasks:
                print(f"The no {key} task is \"{tasks[key]}\"") 
                input()
                break
            elif key.lower() == "back" :
                break
            else:
                print("you entered invalid task number! try again.")
                continue

    elif action == "3":
        print("All task printed!")
        if not tasks:
            print("Thers no task to show!")
            input()
        else:
            for i in tasks:
                print(f"Your no {i} task is {tasks[i]}")
            input("press enter to go back")


    elif action == "4":
        while True:
            key = input("Enter the no of task u want to delet: ")
            if key in tasks:
                del tasks[key]
                print(f"Task no {key} is deleted!")
                input()
                break
            elif key == "back":
                break
            elif key not in tasks:
                print("This no of task does not exist! Try again.")
                continue
    
    elif action == "5":
        tasks = dict()
        with open("data.json","w") as f:
            json.dump(tasks,f)
        print("All task cleared!")
        input()
    
    elif action.lower() == "exit":
        break
            
print("App clossing!")
time.sleep(1)