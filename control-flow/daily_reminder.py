# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
Priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match Priority:
    case "high":
        if time_bound == "yes":
            Reminder = f"High priority task: {task} that requires immediate attention today!"
        else:
            Reminder = f"High priority task: {task}"
    case "medium":
        if time_bound == "yes":
            Reminder = f"Medium priority task: {task} that needs to be done today!"
        else:
            Reminder = f"Medium priority task: {task}"
    case "low":
        if time_bound == "yes":
            Reminder = f"Low priority task: {task} that should be done today!"
        else:
            Reminder = f"Low priority task: {task}"
    case _:
        print("Invalid priority level. Please try again.")
        exit()

# Provide a Customized Reminder
print(Reminder:)