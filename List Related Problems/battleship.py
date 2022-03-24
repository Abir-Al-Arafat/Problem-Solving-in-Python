# The following is useful as part of a program to play Battleship. Write a program that creates and prints a 10 X 10 list that consists of random zeroes and ones. Then ask the user to enter a row and column number. If the entry in the list at that row and column is a one, the program should print Hit and otherwise it should print Miss.

from random import randint

row = int(input("Enter row no.: "))  # asking user to enter row number
column = int(input("Enter column no.: "))  # asking user to enter column number

# initializing 2D list using list comprehension
ship = [[randint(0, 1) for column in range(10)]for row in range(10)]

# checking condition using the row column input
if ship[row][column] == 1:
    print("Hit")
    ship[row][column] += 1  # adding 1 to the element which has been hit
else:
    print("Miss")
    ship[row][column] -= 1  # subtracting 1 from the element which has been missed

# running for loop to print the 2d list in row column format
for r in ship:
    for c in r:
        print(c, end=" ")
    print()
