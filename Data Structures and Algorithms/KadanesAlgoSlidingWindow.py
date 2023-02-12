# write a function which takes an array as input
# and returns the left(beginning) and right(ending) index of the maximum sub-array sum
# assuming there is only one result

# Sliding Window variation of kadane's algo

array = [3, -2, 1, -3, 2, 4, -3, -9]


def sliding_window(array):
    maxSum = array[0]
    sum = 0
    # setting the indices to 0
    maxLeft, maxRight = 0, 0
    left = 0

    for right in range(len(array)):
        # checking if the result gives a negative value
        if sum < 0:
            sum = 0
            # changing the beginning index
            left = right
        # adding value in each iteration
        sum += array[right]

        # checking if maximum result is found
        if sum > maxSum:
            # setting the maximum result
            maxSum = sum
            # setting the indices
            maxLeft = left
            maxRight = right
    # returning the indices
    return [maxLeft, maxRight]


print(sliding_window(array))
