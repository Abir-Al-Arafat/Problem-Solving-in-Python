# implement binary search
# hint: binary search is always done on sorted arrays
# write a function which takes an array and a target value as input and finds the index of that target value and returns it. if the value doesn't exist, it returns a -1.

from random import randint

# array = [1, 3, 3, 4, 5, 6, 7, 8]
# target = 9


def binarySearch(array, target):
    # since binary search runs on sorted arrays
    array = sorted(array)

    # variables for first and last index
    left = 0
    right = len(array) - 1

    while left <= right:
        # middle index
        mid = (left+right) // 2

        if target > array[mid]:
            # left index skips to middle index
            left = mid + 1

        elif target < array[mid]:
            # right index skips to middle index
            right = mid - 1

        else:
            # returns the index
            return mid

    # returns -1 if the value doesnt exist
    return -1


array = [randint(1, 10) for i in range(10)]
target = randint(1, 10)

print(target)
print(sorted(array))

print(binarySearch(array, target))
