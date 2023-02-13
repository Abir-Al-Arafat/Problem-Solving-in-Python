# Find the length of the longest sub-array, with the same value in each position
# Time Complexity: O(n)

from random import randint
array = [randint(1, 3) for i in range(10)]
print(array)
# array = [4, 2, 2, 3, 3, 3]


def longestSubArray(array):
    # setting the left boundary and lengths to 0
    left = 0
    length = 0
    maxLength = 0
    for right in range(len(array)):
        # checking if the sub array has same values
        if array[left] == array[right]:
            length += 1
        # changing left boundary and length if the value doesnt match
        else:
            left = right
            length = 1
        # setting the max length
        if length > maxLength:
            maxLength = length

    return maxLength

# another approach


def longestSubArray2(array):
    # setting the left boundary and length to 0
    left = 0
    length = 0

    for right in range(len(array)):
        if array[left] != array[right]:
            left = right

        length = max(length, right-left+1)

    return length


print(longestSubArray(array))
print(longestSubArray2(array))
