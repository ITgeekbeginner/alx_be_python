def main():
    # Prompt for a single task
    Task = input("Please enter your task: ")
    Priority = input("Please enter the priority level (high/medium/low): ").lower()
    Time_bound = input("Is this task time-bound? (yes/no): ").lower()

    # Initialize reminder message
    reminder = f"Reminder: You have to '{Task}' with a priority level of '{Priority}'."

    # Process the Task Based on Priority
    match Priority:
        case "high":
            reminder += " This task is of high priority!"
        case "medium":
            reminder += " This task is of medium priority."
        case "low":
            reminder += " This task is of low priority."
        case _:
            reminder += " Priority level is not recognized."

    # Modify the reminder if the task is time-bound
    if Time_bound == "yes":
        reminder += " This requires immediate attention today!"

    # Provide a customized reminder
    print(reminder)

if __name__ == "__main__":
    main()

