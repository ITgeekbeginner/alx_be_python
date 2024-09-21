pattern_length = int(input("Enter the size of the pattern:"))

if pattern_length <= 0:
    print("Please enter a positive integer.")
else:
    # Draw the Pattern
    row = 0
    while row < pattern_length:
        for col in range(pattern_length):
            print("*", end="")
        print()  # Move to the next line after completing the row
        row += 1