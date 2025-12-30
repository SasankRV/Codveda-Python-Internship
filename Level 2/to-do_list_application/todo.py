import json
import os

FILE_NAME = "tasks.json"

#loading the tasks into the list
def load_tasks():
   if not os.path.exists(FILE_NAME):
      return []
   with open(FILE_NAME, "r") as file:
      return json.load(file)

#saving the tasks  
def save_tasks(tasks):
   with open(FILE_NAME, "w") as file:
      json.dump(tasks, file, indent=4)


#adding a task in todo list
def add_task():
   task_name = input("Enter the task name:").strip()
   if task_name == "":
      print("Task cannot be empty.")
      return
   
   tasks = load_tasks()
   tasks.append({"task": task_name, "done": False})
   save_tasks(tasks)
   print("Task added successfully.")

#viewing the tasks
def view_tasks():
   tasks = load_tasks()
   if not tasks:
      print("No tasks available.")
      return
   
   print("\n Your Tasks:")
   for index, task in enumerate(tasks, start=1):
      status = "Done" if task["done"] else "Pending"
      print(f"{index}.{task['task']} - {status}")


#marking tasks as done
def mark_task_done():
   tasks = load_tasks()
   if not tasks:
      print("No tasks to mark.")
      return
   
   view_tasks()
   try:
      task_num = int(input("Enter task number to mark as done: "))
      tasks[task_num - 1]["done"] = True
      save_tasks(tasks)
      print("Task marked as completed.")
   except (ValueError, IndexError):
      print("Invalid task number.")

#deleting a task
def delete_task():
   tasks = load_tasks()
   if not tasks:
      print("No tasks to delete.")
      return
   
   view_tasks()
   try:
      task_num = int(input("Enter task number to delete: "))
      removed = tasks.pop(task_num - 1)
      save_tasks(tasks)
      print(f"Task '{removed['task']}' deleted.")
   except (ValueError, IndexError):
      print("Invalid task number.")


#main menu
def main():
   while True:
      print("\n--- TO-DO LIST MENU ---")
      print("1. Add Task")
      print("2. View Tasks")
      print("3. Mark Task as Done")
      print("4. Delete Task")
      print("5. Exit")
      
      choice = input("Choose an option (1-5): ")

      if choice == "1":
         add_task()
      elif choice == "2":
         view_tasks()
      elif choice == "3":
         mark_task_done()
      elif choice == "4":
         delete_task()
      elif choice == "5":
         print("Exiting To-Do List. Goodbye!!")
         break
      else:
         print("Invalid choice. Please try again.")



if __name__ == "__main__":
   main()