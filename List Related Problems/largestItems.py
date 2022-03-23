# Write a program that uses two lists of the same length. Then create a new list where the entry at each index in the new list is the larger of the entries at index of the user’s two lists. For instance, if the two lists are [1,25,3] and [18,2,30], then new list would be [18,25,30].
# L1 = [1,25,3]
# L2 = [18,2,30]

L1 = [1, 25, 3]
L2 = [18, 2, 30]

# declaring an empty list
largest = []

# running a for loop to iterate over items
for index in range(len(L1)):
    if L1[index] > L2[index]:
        largest.append(L1[index])
    else:
        largest.append(L2[index])

# printing the list
print(largest)
