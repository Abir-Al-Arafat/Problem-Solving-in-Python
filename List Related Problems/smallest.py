# Use list of numbers below. Then print out the smallest thing in the list and the first index at which it appears in the list. L= [34,34,23,26,35,37,89,56,48,30,48,19,97,40]

# declaring a list
L = [34, 34, 23, 26, 35, 37, 89, 56, 48, 30, 48, 19, 97, 40]

# initializing a variable to 0
small = 0
# running a for loop

for index in range(len(L)):
    # checking if the smallest number is found or not
    if L[index] < L[small]:
        small = index

print("smallest number", L[small], "which is in index", small)
