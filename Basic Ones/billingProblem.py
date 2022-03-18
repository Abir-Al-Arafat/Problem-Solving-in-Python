# Write a program to ask the user for a starting hour and ending hour, both given in 24-hour format (e.g., 1 pm is 13, 2 pm is 14, etc.). The charge to use the service is $5.50 per hour. Print out the user’s total bill. You can assume that the service will be used for at least 1 hour and never more than 23 hours.


# taking input for starting hour
starting = eval(input("enter a starting hour (between 0-23): "))
# taking input for ending hour
ending = eval(input("enter an ending hour (between 0-23): "))

# checking if the starting and ending hour is between 1-24 or not
if 1 <= starting < 24 and 1 <= ending < 24:
    if starting < ending:
        print("Total cost of ", ending-starting,
              "hour is: ", (ending-starting)*5.50, "$")
    else:
        print("Total cost is: ", (24+ending)-starting)
else:

    print("the starting and ending hour has to be between 0-23")
