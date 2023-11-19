from src import todo_functions as todo
import json



while True:
    print("Type help or ? for print command") 
    print(f"Location: {todo.location}")
    command = input("command >>> ")
    command = command.split(" ")
    parameter = " ".join(command[1:])

    if todo.location == "Home":
        if command[0] == "create":
            todo.createToDo(parameter)
        elif command[0] == "delete":
            todo.deleteToDo(parameter)
        elif command[0] == "open":
            if todo.openToDo(parameter):
                todo.location = "ToDo"
                todo.openedToDo = parameter
    elif todo.location == "ToDo":
        if command[0] == "back":
            todo.location = "Home"
            todo.openedToDo = None
        elif command[0] == "done":
            todo.taskAction(parameter, "Selesai")
        elif command[0] == "undone":
            todo.taskAction(parameter, "Tertunda")


    
    if command[0] == "exit":
        break
    elif command[0] == "view":
        if todo.location == "ToDo": 
            todo.viewTask(todo.check(todo.openedToDo))
            continue
        todo.view()
