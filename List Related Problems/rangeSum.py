# Write a program that first creates and prints a 6 X 6 list of random zeroes, ones, and twos. Then ask the user to enter a starting row, ending row, starting column, and ending column, and print out the sum of all the entries in the list within the range specified by the user.

from random import randint
from unittest import result

# initializing a 6X6 list by random numbers using list comprehension
inp = [[randint(0, 2) for column in range(6)]for row in range(6)]

# asking the user for starting of row index
rowStart = int(input("starting index of row: "))
# asking the user for ending of row index
rowEnd = int(input("ending index of row: "))
# asking the user for starting of column index
colStart = int(input("starting index of column: "))
# asking the user for ending of column index
colEnd = int(input("ending index of column: "))

result = 0

for r in range(rowStart, rowEnd+1):
    for c in range(colStart, colEnd+1):
        # adding the values of user defined row and column indices
        result += inp[r][c]


print(result)  # printing the final result

# printing the initialized list in row column format
for r in inp:
    for c in r:
        print(c, end=" ")
    print()
