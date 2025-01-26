class Task:
    def __init__(self,description):
        self.description=description 
        self.done = False 

    def mark_done(self):
        self.done= True 
    def edit_task(self,new_description): 
        self.description=new_description
    def __str__(self): 
        status= "DONE" if self.done else "Not Done"
        return f"{self.description} (status: {status})"
    
class Todolist:
    def __init__(self):
      self.tasks=[] 
      
    def add_task(self,task_descriptions):
        for desc in task_descriptions:
            task=Task(desc)
            self.tasks.append(task)  
            print(f"'{desc}' added to the list")

    def delete_task(self,tsk_nums):
        tsk_nums=sorted(set(tsk_nums),reverse=True) 
        for tsk_num in tsk_nums: 

            if 0< tsk_num <= len(self.tasks): 
             deleted_task = self.tasks.pop(tsk_num-1) 
             print(f"Task '{deleted_task.description}' successfully deleted.")
            else:
             print("invalid task number") 
    def view_task(self): 
        if not self.tasks: 
            print("No existing tasks")
        else:
            print("To-do list:") 
            for i,task in enumerate(self.tasks,1): 
                print(f"{i}: {task}") 
    def edit_task(self,tsk_num,new_description):
        if 0< tsk_num <= len(self.tasks):
            self.tasks[tsk_num-1].edit_task(new_description) 
            print(f"Task {tsk_num} updated successfully.")
        else:
            print("Invalid task number")
    def mark_task_done(self,tsk_nums): 
        tsk_nums =sorted(set(tsk_nums)) 
        for tsk_num in tsk_nums:  
            if 0 <tsk_num <= len(self.tasks): 
                self.tasks[tsk_num-1].mark_done() 
                print(f"Task{tsk_num} marked as done.")
            else:
                print("invalid task number") 
class Program:
    def __init__(self):
        self.todolist = Todolist() 
    def start(self):
      while True: 
       
        print("\nMAIN MENU")
        print("1.Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Tasks as done")
        print("5. Delete Tasks")
        print("6. Exit")

        choice = input("Choose any option: 1/2/3/4/5/6: ") 

        if choice == "1":
           task_descriptions = input("Enter the task(use comma for more than one task) : ").split(',') 
           task_descriptions=[desc.strip() for desc in task_descriptions if desc.strip()] 
           self.todolist.add_task(task_descriptions) 
        elif choice == "2": 
           self.todolist.view_task() 
        elif choice=="3": 
            try:
                tsk_num =int(input("Enter the task number to edit: ")) 
                new_description = input("Enter new description")
                if new_description:
                    self.todolist.edit_task(tsk_num,new_description) 
                else:
                    print("No changes made to the task.") 
            except ValueError:
                print("please enter a valid tas number.") 
        elif choice=="4":       
            try:   
                 tsk_nums=input("Enter task numbers to Mark tasks as 'done'(use comma for more than one task : ") 
                 tsk_nums=[int(num.strip()) for num in tsk_nums.split(',')] 
                
                 self.todolist.mark_task_done(tsk_nums)
            except ValueError:
                print("please enter  valid task numbers")

        elif choice=="5":
            try:    
                tsk_nums=input("Enter task number to delete(use comma for more than one task) :")
                tsk_nums =[int(num.strip()) for num in tsk_nums.split(',')] 
                self.todolist.delete_task(tsk_nums)
            except ValueError:
                print("please enter a valid option")
        elif choice=="6": 
            print("Thanks For Visiting")
            break 
        
        else: 
            print("Invalid option") 
        
Program().start() 