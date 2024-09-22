# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
Priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match Priority:
    case "high":
        if time_bound.lower() == "yes":
            reminder = f"High priority task: {task} that requires immediate attention today!"
        else:
            reminder = f"High priority task: {task}"
    case "medium":
        if time_bound.lower() == "yes":
            reminder = f"Medium priority task: {task} that needs to be done today!"
        else:
            reminder = f"Medium priority task: {task}"
    case "low":
        if time_bound.lower() == "yes":
            reminder = f"Low priority task: {task} that should be done today!"
        else:
            reminder = f"Low priority task: {task}"
    case _:
        print("Invalid priority level. Please try again.")
        exit()

# Provide a Customized Reminder
print(reminder)