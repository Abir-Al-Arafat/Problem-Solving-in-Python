# Write a Python program to filter a list of integers using Lambda.

# Original list of integers:

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the list:

# [2, 4, 6, 8, 10]

# Odd numbers from the list:

# [1, 3, 5, 7, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers: ", evenNumbers)

oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd Numbers", oddNumbers)
