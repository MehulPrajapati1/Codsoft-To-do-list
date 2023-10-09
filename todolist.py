# Initialize an empty to-do list
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added.")

# Function to remove a task from the list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view all tasks in the list
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")