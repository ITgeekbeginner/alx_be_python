number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
for k in range(1, 11):
    product = number * k
    print(f"{number} * {k} = {product}")
