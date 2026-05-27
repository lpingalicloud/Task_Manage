from tasks import*
def ChooseTask(nums):
    if nums==1:
        addt = (input("type the task you would like to add/update :")).lower()
        comps =(input("what is the current completion status of this project :")).lower()        
        taskone(addt,comps)
    if nums==2:
        tasktwo()
    if nums==3:
        taskdelete = (input("which task would you like to delete? :")).lower()
        taskthree(taskdelete)

        



        
    