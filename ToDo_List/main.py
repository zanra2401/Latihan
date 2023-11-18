from src import todo_functions as todo
import json



while True:
    print("Type help or ? for print command") 
    print(f"Location: {todo.location}")
    command = input("command >>> ")
    command = command.split(" ")
    parameter = command[1:]

    if todo.location == "Home":
        if command[0] == "view":
            if todo.location == "ToDo":
                pass
                continue
            todo.view()
        elif command[0] == "create":
            todo.createToDo(" ".join(parameter))
        elif command[0] == "delete":
            todo.deleteToDo(" ".join(parameter))
        elif command[0] == "open":
            if todo.openToDo(" ".join(parameter)):
                todo.location = "ToDo"
    elif todo.location == "ToDo":
        if command[0] == "done":
            todo.doneTask(" ".join(parameter))
        elif command[0] == "back":
            todo.location = "Home"
    
    
    if command[0] == "exit":
        break
