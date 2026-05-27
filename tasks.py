import pathlib
import json
import os
def tasktwo():
    try:
        with open("task.json","r",encoding="utf-8") as taskfile:
            tasklist = json.load(taskfile)
        print(tasklist)
    except FileNotFoundError:
        print("there are currently no active tasks. Please add new ones")
        
        
def taskone(addtask, compstat):
    try:
        with open("task.json", "r", encoding="utf-8") as taskfile:
            taskdict = json.load(taskfile)      
    except FileNotFoundError:
        taskdict={}       
    taskdict[addtask] = compstat
    with open("task.json", "w", encoding="utf-8") as taskfile:
        json.dump(taskdict,taskfile)
    print("added")
    
def deleteTask(tasklist,taskdel):
    if tasklist.get(taskdel) != None:
        del tasklist[taskdel]
        print("task deleted")
    else:
        print("\n\nthat task doesn't exist\n\n")
    with open("task.json","w",encoding="utf-8") as taskfile:
        json.dump(tasklist,taskfile)
    
def taskthree(taskdel):
    try:
        with open("task.json","r",encoding="utf-8") as taskfile:
            tasklist = json.load(taskfile)
            deleteTask(tasklist, taskdel)
        if tasklist=={}:
            os.remove("task.json")                    
    except FileNotFoundError:
        print("there are currently no active tasks. Please add new ones before deleting")