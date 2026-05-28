import json
import os
def tasktwo():
    try:
        with open("task.json","r",encoding="utf-8") as taskfile:
            tasklist = json.load(taskfile)
        print(tasklist)
    except FileNotFoundError:
        print("there are currently no active tasks. Please add new ones")
    except json.JSONDecodeError as e:
        print(e)
        print("removing the corrupted file")
        os.remove("task.json")
    
        
        
def taskone(addtask, compstat:int):
    completion=f"{compstat}%"    
    try:
        with open("task.json", "r", encoding="utf-8") as taskfile:
            taskdict = json.load(taskfile)      
    except FileNotFoundError:
        taskdict={}
    except json.JSONDecodeError as e:
        print(e)
        print("removing the corrupted file")
        os.remove("task.json")
        return None                
    taskdict[addtask] = completion
    with open("task.json", "w", encoding="utf-8") as taskfile:
        json.dump(taskdict,taskfile)
    print(f"\n\n added task \"{addtask}: {completion}\"\n\n")
    
def deleteTask(tasklist,taskdel):
    try:
        del tasklist[taskdel]
        print(f"\n\ndeleted task \"{taskdel}\"\n\n")
    except KeyError:
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
    except json.JSONDecodeError as e:
        print(e)
        print("removing the corrupted file")
        os.remove("task.json")