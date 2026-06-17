import json
import os
       
class Tasks():
    def __init__(self,taskname="",completion=0):
        self.taskname = taskname
        self.completion = completion
    def fileopenread(self):
        try:
            with open("task.json", "r", encoding="utf-8") as taskfile:
                taskdict = json.load(taskfile)
            return taskdict    
        except FileNotFoundError:
            taskdict={}
            return taskdict
        except json.JSONDecodeError as e:
            print(e)
            print("removing the corrupted file")
            os.remove("task.json")
            return None  
    def tasktwo(self):
        file = self.fileopenread()
        if self.fileopenread != None and self.fileopenread != {}:
            print(self.fileopenread())
        elif self.fileopenread == {}:
            print("Currently no new tasks, please add new ones")
            
        
    def taskchosen(self):
        pass
    def taskone(self):
        completion=f"{self.completion}%"
        task = self.taskname
        tasklist = self.fileopenread()
        tasklist[task] = completion
        with open("task.json", "w", encoding="utf-8") as taskfile:
            json.dump(tasklist,taskfile)
        print(f"\n\n added task \"{task}: {completion}\"\n\n")
    
    def deleteTask(self,tasklist):
        try:
            del tasklist[self.taskname]
            print(f"\n\ndeleted task \"{self.taskname}\"\n\n")
        except KeyError:
            print("\n\nthat task doesn't exist\n\n")
        with open("task.json","w",encoding="utf-8") as taskfile:
            json.dump(tasklist,taskfile)
        
    def taskthree(self, taskdel):
        file = self.fileopenread()
        if file != None and file != {}:
            tasklist = file
            self.deleteTask(tasklist)

        else:
            print("there are currently no active tasks. Please add new ones before deleting")
            os.remove("task.json")
        
        
        