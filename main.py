'''simple to do list project
Add tasks

Practice string handling and lists
View tasks

Practice loops and printing
Mark tasks as complete

Practice lists and conditional statements
Delete tasks

Practice list operations
'''
tasks = [] # initialize an empty list to store tasks
def add_task(): # define a function to add tasks
    task = input("Enter a task: ") 
    tasks.append(task) # add the task to the list
    print(f"Task '{task}' added successfully.") # print a success message

def view_tasks(): # define a function to view tasks
    if tasks:     # check if the list is not empty
        print("Tasks:")  # print the header 
        for index, task in enumerate(tasks, start=1):  # enumerate the tasks- means add a number/index to each task
            print(f"{index}. {task}") # print the task with its number/index
    else:
        print("No tasks found.") # print a message if the list is empty

def mark_complete(): # define a function to mark tasks as complete
    view_tasks()  # call the view_tasks function to display the tasks
    task_number = int(input("Enter the number of the task to mark as complete: ")) # get the task number from the user
    if 1 <= task_number <= len(tasks):  # check if the task number is valid
        task_removal = tasks.pop(task_number - 1) # remove the task from the list, also subtract 1 because the index starts from 0
        print(f"Task '{task_removal}' marked as complete.") # print a success message
    else:
        print("Invalid task number.") # print an error message

def delete_task(): # define a function to delete tasks
    view_tasks() # call the view_tasks function to display the tasks
    task_number = int(input("Enter the number of the task to delete: ")) # get the task number from the user
    if 1 <= task_number <= len(tasks): # check if the task number is valid
        task_removal = tasks.pop(task_number - 1) # remove the task from the list, also subtract 1 because the index starts from 0
        print(f"Task '{task_removal}' deleted.") # print a success message
    else:
        print("Invalid task number.") # print an error message

# main program loop
while True:
    print("1. Add Task") # print the menu options
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ") # get the user's choice

    if choice == "1": # if the user chooses to add a task
        add_task() # call the add_task function
    elif choice == "2": # if the user chooses to view tasks
        view_tasks() # call the view_tasks function to display the tasks
    elif choice == "3": # if the user chooses to mark a task as complete
        mark_complete() # call the mark_complete function
    elif choice == "4": # if the user chooses to delete a task
        delete_task() # call the delete_task function
    elif choice == "5": # if the user chooses to quit
        print("Goodbye!") # print a goodbye message
        break # exit the loop
    else: # if the user enters an invalid choice
        print("Invalid choice. Please try again.")