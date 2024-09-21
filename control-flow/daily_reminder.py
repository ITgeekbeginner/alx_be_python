task= input("Enter your task: ")
Priority = input("priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Generate reminder based on priority and time sensitivity
match Priority:
    case "high":
        reminder = "This is a high-priority task."
    case "medium":
        reminder = "This is a medium-priority task."
    case "low":
        reminder = "This is a low-priority task."
    case _:
        reminder = "priority not recognized."

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(f"Reminder: {reminder} Task: {task}")
