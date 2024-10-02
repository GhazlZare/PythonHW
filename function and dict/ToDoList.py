def add_task(tasks):
    name = input("Enter the new task name: ").lower()
    if name in tasks:
        print("Already exists. Choose another one.")
    else:
        tasks[name] = {"status": False, "duration": None}
        print("Added")


def display_tasks(tasks):
    if not tasks:
        print("Empty")
    for key, value in tasks.items():
        print(3*"*" + key + 3*"*")
        for k, v in value.items():
            print(f"{k} : {v}")



def remove_task(tasks):
    name = input("Please enter the task name you want to remove: ").lower()
    if name in tasks:
        tasks.pop(name)
        print("Removed!")
    else:
        print("Name not found!")


def edit_task(tasks):
    name = input("Enter the name you want to edit: ").lower()
    if name in tasks:
        new_name = input("Enter the new name: ").lower()
        if new_name not in tasks:
            tasks[new_name] = tasks.pop(name)
            print("Updated")
        else:
            print("Already exists!")
    else:
        print("Name not found!")


def search_task(tasks):
    name = input("Enter the name you want to search: ").lower()
    if name in tasks:
        details = tasks[name]
        print(f"name: {name}, task status: {details['status']}, task duration: {details['duration']}")
    else:
        print("Not found")


def mark_task_done(tasks):
    name = input("Enter the task name to mark as done: ").lower()
    if name in tasks:
        if tasks[name]["status"] == False:
            tasks[name]["status"] = True
            start_time = input("Enter the time you started (e.g., 9:00): ").split(":")
            end_time = input("Enter the time you finished (e.g., 9:00): ").split(":")
            start_time_h, start_time_m = int(start_time[0]), int(start_time[1])
            end_time_h, end_time_m = int(end_time[0]), int(end_time[1])

            if end_time_m < start_time_m:
                end_time_h -= 1
                end_time_m += 60

            difference_h = end_time_h - start_time_h
            difference_m = end_time_m - start_time_m
            duration = f"{difference_h}:{difference_m}"

            tasks[name]["duration"] = duration
            print(f"The {name} task is done in {tasks[name]['duration']}")
    else:
        print("Name not found")


def display_details(tasks):
    all_tasks = len(tasks)
    done_tasks = sum(1 for task in tasks.values() if task["status"])
    undone_tasks = all_tasks - done_tasks

    total_hours, total_minutes = 0, 0
    for details in tasks.values():
        if details["status"] and details["duration"]:
            h, m = map(int, details["duration"].split(":"))
            total_hours += h
            total_minutes += m

    total_hours += total_minutes // 60
    total_minutes %= 60

    print(f"all tasks: {all_tasks}, completed: {done_tasks}, not completed: {undone_tasks}, hours worked: {total_hours}:{total_minutes}")


def help_menu():
    print('''To do anything you should enter the number next to the button.
    1. Add a new and unique task.
    2. Display all tasks, their status, and duration.
    3. Remove a task by name.
    4. Edit an existing task name.
    5. Search for a task by name and display its details.
    6. Mark a task as done and enter start and end time to calculate duration.
    7. Display total tasks, done/undone tasks, and total work hours.
    9. Exit the program.''')


def main():
    tasks = {}

    while True:
        answer = int(input("Please enter the task number that you want to do: 1.add a new task 2.display all tasks 3.remove a task 4.edit a task 5.search 6.mark a task as done 7.Display details 8.help 9.Exit "))
        if answer == 1:
            add_task(tasks)
        elif answer == 2:
            display_tasks(tasks)
        elif answer == 3:
            remove_task(tasks)
        elif answer == 4:
            edit_task(tasks)
        elif answer == 5:
            search_task(tasks)
        elif answer == 6:
            mark_task_done(tasks)
        elif answer == 7:
            display_details(tasks)
        elif answer == 8:
            help_menu()
        elif answer == 9:
            break
        else:
            print("Out of range")


if __name__ == "__main__":
    main()
