
# Task 1: Check if a Number is Even or Odd

try:
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")




# Task 2: Sum of integers from 1 to 50

total_sum = 0

for i in range(1, 51):
    total_sum += i

print("The sum of integers from 1 to 50 is:", total_sum)
