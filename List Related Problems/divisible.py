# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# declaring an empty list
output = []

# running a for loop
for i in range(2000, 3201):
    # checking condition
    if (i % 7 == 0 and i % 5 != 0):
        # adding values to the empty list if conditions are met
        output.append(str(i))

# printing values
print(",".join(output))
