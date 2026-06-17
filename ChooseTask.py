from tasks import*
def choose_task(nums):
    if nums==1:
        try:
            addt = (input("\ntype the task you would like to add/update :")).lower()
            comps =int((input("\nwhat is the current completion % of this project :")))    
            task = Tasks(addt, comps)
            task.taskone()
        except ValueError:
            print("please type the number percentage without the % sign")
    if nums==2:
        task = Tasks()
        task.tasktwo()
    if nums==3:
        taskdelete = (input("which task would you like to delete? :")).lower()
        task = Tasks(taskdelete)
        task.taskthree(taskdelete)
    elif nums>4: 
        print("please type a number from 1 to 4 for options")

        



        
    