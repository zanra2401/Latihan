import json

location = "Home"
openedToDo = None

def read():
    with open("todo/todo.json", 'r') as f:
        data = json.load(f)["todo"]
    return data

def write(data):
    with open("todo/todo.json", 'w') as f:
        json.dump(data, f, indent = 2)

def view():
    print("$ To Do List ^_^")
    print()
    todo = read()
    for i in range(len(todo)):
        print(f"{i+1}. {todo[i]['name']} {checkStatus(todo[i]['task'])} ")

    print()

        
def checkStatus(task):
    totalTask = len(task)
    if totalTask < 1:
        return "[0%]"
    completedTask = 0 
    for i in task:
        if i["status"] == "Selesai":
            completedTask += 1

    percentage = ((completedTask / totalTask) * (100/100)) * 100

    if percentage < 1:
        return "[" + str(percentage) + "%" + "]"
         
    return "[" + str(int(percentage)) + "%" + "]"

def createToDo(nama):
    if check(nama)  != None:
        print(f"ToDo list bernama {nama} sudah ada")
        return

    data = read() 
    todo = { "name" : nama, "task" : []}
    data.append(todo)
    data = {"todo" : data}

    write(data)

def deleteToDo(nama):

    data = read()

    delete = check(nama)
    if delete == None:
        print(f"ToDo list bernama {nama} tidak ada")
        return
            
    del data[delete]

    data = { "todo" : data }

    write(data)


def check(nama):
    data = read()

    index = 0

    for i in data:
        if i["name"] == nama:
            return index
        index += 1

    return None

def openToDo(nama):
    if check(nama) == None:
        print(f"ToDo list bernama {nama} tidak ada")
        return

    viewTask(check(nama))
    return True

def viewTask(index):

    data = read()[index]

    print("^_^ Task !!!")
    print(f"Progres {checkStatus(data['task'])}")
    print()

    no = 1


    for i in data["task"]:
        done = "[ ]"
        if i["status"] == "Selesai":
            done = "[*]"
            
        print(f"{done} {i['description']}")
        no += 1
    print()

def doneTask(task):
    data = read()

