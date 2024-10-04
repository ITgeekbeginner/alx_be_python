def safe_divide(numerator, denominator):
    try:
        numerator = int(input("Enter the first number: "))
        denominator = int(input("Enter the second number: "))
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.") 
    except ValueError:
        print("Error: Please enter numeric values only.")

safe_divide()