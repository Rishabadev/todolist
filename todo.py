class Task:
    def __init__(self,description):
        self.description=description #stores task description
        self.done = False # set the default status as "not done".

    def mark_done(self):
        self.done= True #marks the done by setting 'done' to true
    def edit_task(self,new_description): #updates the task description.
        self.description=new_description
    def __str__(self): #returns string representtion of the task description with current status.
        status= "DONE" if self.done else "Not Done"
        return f"{self.description} (status: {status})"
    
class Todolist:
    def __init__(self): # Constructor to initialize todolist.
      self.tasks=[] #to initialize an empty list to store tasks
      
    def add_task(self,task_descriptions): #function to add a new task to todolist.
        for desc in task_descriptions:
            task=Task(desc)
            self.tasks.append(task)  #using append method to add a new task into the list.
            print(f"'{desc}' added to the list")

    def delete_task(self,tsk_nums): #function to delete a task from the todolist.
        tsk_nums=sorted(set(tsk_nums),reverse=True) #sorts task numbers in descending order to avoid index issues.
        for tsk_num in tsk_nums: #iterate through each task number to be deleted.

            if 0< tsk_num <= len(self.tasks): #to check whether the entered task number is within the valid range.
             deleted_task = self.tasks.pop(tsk_num-1) #deletes the task specified position and it is adjusted accordingly.
             print(f"Task '{deleted_task.description}' successfully deleted.")
            else:
             print("invalid task number") # To print if the entered task number is out of range.
    def view_task(self): # To show all tasks in the todolist.
        if not self.tasks: # To display the message, if no tasks added. 
            print("No existing tasks")
        else:
            print("To-do list:") #Title for to do list
            for i,task in enumerate(self.tasks,1): # enumerate throgh each tasks, index starting from 1.
                print(f"{i}: {task}") # diplays each task with its corresponding index.
    def edit_task(self,tsk_num,new_description): #cheecks if task number is valid
        if 0< tsk_num <= len(self.tasks):
            self.tasks[tsk_num-1].edit_task(new_description) #updates task description.
            print(f"Task {tsk_num} updated successfully.")
        else:
            print("Invalid task number")
    def mark_task_done(self,tsk_nums): #fuction to mark the task as done.
        tsk_nums =sorted(set(tsk_nums)) #sorts the task number to avoid duplicates.
        for tsk_num in tsk_nums:  #iterate through each task number
            if 0 <tsk_num <= len(self.tasks): #check if the task number is valid
                self.tasks[tsk_num-1].mark_done() #marks the specified task as done
                print(f"Task{tsk_num} marked as done.")
            else:
                print("invalid task number") # prints an invalid message for entering wrong task number.
class Program: #constructor to initialize the program class.
    def __init__(self):
        self.todolist = Todolist() #creating an instance of the Todolist class.
    def start(self): #method to start the program.
      while True: #infinite loop to keep the program running until user chooses to exit.
       # displays the main menu( options).
        print("\nMAIN MENU")
        print("1.Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Tasks as done")
        print("5. Delete Tasks")
        print("6. Exit")

        choice = input("Choose any option: 1/2/3/4/5/6: ") #prompt the user to choose an option from the menu.

        if choice == "1": #option to add new task.
           task_descriptions = input("Enter the task(use comma for more than one task) : ").split(',') #prompt the user to enter a new task, allowing multiple entries with commas.
           task_descriptions=[desc.strip() for desc in task_descriptions if desc.strip()] # to strip
           self.todolist.add_task(task_descriptions) # calls the add_Task method to add the task into the todolist.
        elif choice == "2": #option to view all tasks.
           self.todolist.view_task() # calls the view_Task method to display all the tasks.
        elif choice=="3": # option to edit task
            try:
                tsk_num =int(input("Enter the task number to edit: ")) #prompt the to enter task number of that specific task
                new_description = input("Enter new description")
                if new_description:
                    self.todolist.edit_task(tsk_num,new_description) #calls the edit_task method to update the task.
                else:
                    print("No changes made to the task.") #informs the user if no changes provideed.
            except ValueError:
                print("please enter a valid tas number.") # to show invalid output.
        elif choice=="4": #option to mark tasks as done.
            try:   
                 tsk_nums=input("Enter task numbers to Mark tasks as 'done'(use comma for more than one task : ") #prompt the user to enter task numbers of the tasks.
                 tsk_nums=[int(num.strip()) for num in tsk_nums.split(',')] #splits the input string by commas to handle multiple tasknumbers
                 # removes any surrounding white-spacce from each number using strip(),
                 #and converts each cleaned string to an integer to create a list of task numbers.
                 self.todolist.mark_task_done(tsk_nums) # Calls the mark_task_done method to update tasks.
            except ValueError:
                print("please enter  valid task numbers") #to handl invalid input.

        elif choice=="5":#option  to delete tasks.
            try:    #prompt the user to enter the task number to delete tasks , allowing multipe entries.
                tsk_nums=input("Enter task number to delete(use comma for more than one task) :")
                tsk_nums =[int(num.strip()) for num in tsk_nums.split(',')] #converts the input task into a list of integers.
                self.todolist.delete_task(tsk_nums) #calls the delete_task method to delete tasks.
            except ValueError:
                print("please enter a valid option") #to handle invalid input.
        elif choice=="6": #option to exit the program.
            print("Thanks For Visiting")
            break # exit the loop and end the  program.
        
        else: 
            print("Invalid option") #to display invalid selection of option.
        
Program().start() # Creates an instance of the program class and calls the start method.
