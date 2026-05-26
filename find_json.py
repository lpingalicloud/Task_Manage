import pathlib
import json
import os
while(True):
    taskname = int(input("task manager. would you like to :\n\t1.Add\n\t2.List\n\t3.delete\n\t4.Quit\nPlease enter your number here :"))
    if(taskname == 4):
        print("Goodbye")
        break
    if(taskname == 1):
        try:
            with open("task.json", "r", encoding="utf-8") as taskfile:
                taskdict = json.load(taskfile)      
        except FileNotFoundError:
            taskdict={}       
        addtask = (input("type the task you would like to add/update :")).lower()
        compstat =(input("what is the current completion status of this project :")).lower()
        taskdict[addtask] = compstat
        with open("task.json", "w", encoding="utf-8") as taskfile:
            json.dump(taskdict,taskfile)
        print("added")
    if(taskname ==2):
        try:
            with open("task.json","r",encoding="utf-8") as taskfile:
                tasklist = json.load(taskfile)
            print(tasklist)
        except FileNotFoundError:
            print("there are currently no active tasks. Please add new ones")
    if(taskname == 3):
        try:
            with open("task.json","r",encoding="utf-8") as taskfile:
                tasklist = json.load(taskfile)
                print(tasklist)
                taskdel = (input("which task would you like to delete? :")).lower()
                if tasklist.get(taskdel) != None:
                    del tasklist[taskdel]
                    print("task deleted")
                else:
                    print("\n\nthat task doesn't exist\n\n")
                with open("task.json","w",encoding="utf-8") as taskfile:
                    json.dump(tasklist,taskfile)
            if tasklist=={}:
                os.remove("task.json")                    
        except FileNotFoundError:
            print("there are currently no active tasks. Please add new ones before deleting")
        
        
        
        
                
            