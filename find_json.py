from ChooseTask import choose_task as ct

if __name__=="__main__":
    while(True):
        try:
            taskname = int(input("""\n        TASK MANAGER
        would you like to :
        \n\t1.Add
        \n\t2.List
        \n\t3.delete
        \n\t4.Quit\n
        Please enter your number here :"""))
            if taskname==4:
                print("\n\nExiting task manager\n\n")
                break
            ct(taskname)
        except ValueError:
            print("please type numbers without any additional signs or letters")


        
        

    
             
            