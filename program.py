# add function
tasks = []
def add_tasks():
    user_task = input("kindly enter your task:\n")
    tasks.append(user_task)
    print("Task added successfully!!!")

# view function method 2
def view_tasks():
     if not tasks:
          print("To-do-list is empty. Please add tasks")
     else:
          for i, task in enumerate(tasks, 1):
               print(f"{i}. {task}")


# menu function
def display_menu():
      print("1.Select 1 to add tasks\n")
      print("2.Select 2 to view tasks\n")
      print("3.Select 3 to update tasks\n")
      print("4.Select 4 to delete tasks\n")
      print("5.Select 5 to exit\n")

# update function
def update():
     # display current tasks
     print("Below are the available tasks")
     view_tasks
     task_number = int(input("kindly Select task to be updated: \n"))
     if 1 <= task_number <= len(tasks):
          updated_task = input("Enter update: \n")
          tasks[task_number - 1] = updated_task
          print("Task updated successfully")

# delete function
def delete():
     view_tasks()
     task_number = int(input("Kindly select task to delete: \n"))
     if 1 <= task_number <= len(tasks):
          delete_task = tasks.pop(task_number - 1)
          print(f"Task '{delete_task}' successfully deleted!!!")
     else:
          print("Task list is empty. Please add task.")

# Exit Function
def exit_task():
     exit(1)
     

# view function method 1
# def view_task():
#      if len(tasks) > 0:
#           print(tasks)
#      else:
#           print("There are no tasks to view")

