# Find the minimum length size of sub-array, where the sum of elements are greater than or equal to the target. Assume all values are positive

array = [2, 3, 1, 2, 4, 3]


def minLenSubArray(array, target):
    left = 0
    total = 0
    # setting a default length
    length = len(array) + 1

    for right in range(len(array)):
        # adding the array element
        total += array[right]
        # checking if the total so far is greater than or equal to the target
        while total >= target:
            # setting minimum length
            length = min(length, (right-left) + 1)
            # deducting before shrinking the boundary
            total -= array[left]
            # shrinking down left boundary
            left += 1
    # checking if the smallest sub array length found or not
    if length == len(array)+1:
        return False

    return length


length = float('inf')
print(minLenSubArray(array, 6))
