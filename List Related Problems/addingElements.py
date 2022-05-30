# Add two lists below using map function with lambda and return output as list.

# Input:

# Output:[101, 202, 303, 404]

list1 = [1, 2, 3, 4]

list2 = [100, 200, 300, 400]


def add_list(list1, list2):
    return [x+y for x, y in zip(list1, list2)]


print(add_list(list1, list2))

# another approach using map functions

# map function takes a function and any number of iterables

addElements = list(map(lambda x, y: x+y, list1, list2))
print("using map function: ", addElements)
