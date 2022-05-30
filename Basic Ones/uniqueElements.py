# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# Unique List : [1, 2, 3, 4, 5]

def unique(list):
    unique_list = []  # initializig empty list
    for element in list:  # running a for loop
        if element not in unique_list:  # checking if the element exists in the list
            unique_list.append(element)  # adding the unique elements
    return unique_list  # returning the list


print(unique([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
