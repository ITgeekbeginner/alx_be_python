FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
   global FAHRENHEIT_TO_CELSIUS_FACTOR
   return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
   global CELSIUS_TO_FAHRENHEIT_FACTOR
   return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
   temperature = input("Enter the temperature to convert: ")
   unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

try:
        temperature = input("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
        temperature = float(temperature)
except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if unit.upper() == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
elif unit.upper() == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
else:
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
