# Write a function to find a non-empty sub-array with the largest sum and return the largest sub-array sum
# sub-array: contiguous array inside of an array

array = [4, -1, 2, -7, 3, 4]

# Time Complexity: O(n^2)


def brute_force(array):
    largestSum = array[0]
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if largestSum < sum:
                largestSum = sum
    return largestSum

# Kadane's algorithm O(n)
# Linear time algorithm


def kadanes_algo(array):
    largestSum = array[0]
    sum = 0
    for val in array:
        sum += val
        if largestSum < sum:
            largestSum = sum
        if sum < 0:
            sum = 0

    return largestSum


print(brute_force(array))
print(kadanes_algo(array))
