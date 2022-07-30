# Write a function called changes_by_one() that takes a list of integers and returns a list of all the indices at which the current value is 1 more than the previous value. For instance,
# if the list is [1,2,5,5,10,11,12,15,16], it would return [1,5,6,8].


# declaring a list of numbers
numbers = [1, 2, 5, 5, 10, 11, 12, 15, 16]

# declaring a function


def changes_by_one(numbers):
    # declaring an empty list
    indices = []
    # running a for loop
    for index in range(len(numbers)-1):
        # checking if the result of the subtraction is 1 or not
        if numbers[index+1]-numbers[index] == 1:
            # adding the indices
            indices.append(index+1)
    # returning the indices
    return indices


print(changes_by_one(numbers))
