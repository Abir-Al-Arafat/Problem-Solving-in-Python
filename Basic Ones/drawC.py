# write a program which asks a user to give a width and height and draw a "C" according to that width and height value. the width and height has to be same

wh = int(input("Give width and height: "))  # taking input from user

# writing a for loop to draw the first row
for i in range(wh):
    print("*", end=" ")

# executing a new line
print()

# subtracting 2 to make the height equal to the width
for i in range(wh-2):
    print("*")

# writing for loop to draw the last row
for i in range(wh):
    print("*", end=" ")
