numerator = int(input(f"Enter the numerator: "))
denominator = int(input(f"Enter the denominator: "))

class safe_divide(numerator, denominator):
    #numerator = int(input("Enter the numerator: "))
    #denominator = int(input("Enter the denominator

    try:
        result = numerator / denominator
        print("The result of the division is {result}")
    except ZeroDivisionError:
       print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Please enter numeric values only")
    
     