# write a program which takes input of range from a user to print even numbers till that range

# 1st method

inp = int(input("Give a range: "))  # taking input from user

# for loop to iterate to the range

for i in range(inp+1):
    # condition to print even numbers
    if i % 2 == 0:
        print(i, end=" ")

print()  # new line
# 2nd method

for i in range(0, inp+1, 2):
    print(i, end=" ")
