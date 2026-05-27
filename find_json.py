import json
from ChooseTask import ChooseTask as ct


while(True):
    taskname = int(input("task manager. would you like to :\n\t1.Add\n\t2.List\n\t3.delete\n\t4.Quit\nPlease enter your number here :"))
    if taskname==4:
        break
    ct(taskname)


        
        

    
             
            