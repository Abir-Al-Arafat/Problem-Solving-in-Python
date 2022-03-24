# Determine if there are consecutive horizontal or vertical zeroes in a random 6x6 list of integers from 0 to 5.

from random import randint

numbers = [[randint(0, 3) for col in range(6)]for row in range(6)]

for r in range(len(numbers)):
    for c in range(len(numbers[r])):
        print(numbers[r][c], end=" ")
    print()

# checking vertically

for row in range(len(numbers)):
    for col in range(len(numbers[row])):
        if numbers[row-1][col] == numbers[row][col] == 0:
            print("consecutive zero found vertically")

# checking horizontally

for row in range(len(numbers)):
    for col in range(len(numbers[row])):
        if numbers[row][col] == numbers[row][col-1] == 0:
            print("consecutive zero found horizontally")
