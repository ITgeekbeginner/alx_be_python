def perform_operation(num1: float, num2: float, operation: str) -> float:
    
    # Check if the operation is valid
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        raise ValueError("Invalid operation. Must be 'add', 'subtract', 'multiply', or 'divide'.")

    # Perform the operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2

