# Given a sorted input array, return the two indices of two elements which sum up to the target value. Assume there is exactly ONE solution

array = [-1, 2, 3, 4, 7, 9]

# time complexity: O(n^2)


def bruteForce(array, target):
    indices = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == target:
                indices.append(i)
                indices.append(j)
                return indices

# time complexity: O(n)


def sumIndices(array, target):
    # setting pointers
    left = 0
    right = len(array) - 1

    # runs until a result is found
    while True:
        # checking if the sum is bigger than the target
        if array[left] + array[right] > target:
            # shifting the pointer
            right -= 1
        # checking if the sum is smaller than the target
        elif array[left] + array[right] < target:
            # shifting the pointer
            left += 1

        else:
            # returning the indices of the elements
            return [left, right]


print(bruteForce(array, 7))
print(sumIndices(array, 7))
