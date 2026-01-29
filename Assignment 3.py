task 1:

def factorial(n):
    """
    This function takes a number as input
    and returns its factorial.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Sample function call
number = 5
output = factorial(number)
print(f"Factorial of {number} is: {output}")


Task 2:


import math

try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive number greater than zero.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

        print(f"Square root of {number}: {square_root}")
        print(f"Natural logarithm of {number}: {natural_log}")
        print(f"Sine of {number} (in radians): {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid number.")