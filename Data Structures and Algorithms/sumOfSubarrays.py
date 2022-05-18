# write a function which takes an array of numbers and returns the largest contigiuous sum of subarray

def sumOfSubArray(numbers):
    current = 0  # initializing the current variable to 0
    maxSoFar = 0  # initializing the max so far variable to 0
    for number in numbers:  # iterating over the numbers
        current += number  # adding each number to the current variable
        if current > maxSoFar:  # checking if the added value is the max value found so far
            maxSoFar = current  # replacing the max value with the current value
    return maxSoFar  # returning the max value


# numbers = [-5, 4, 6, -3, 4, -1]
numbers = [-2, -3, 4, -1, -2, 1, 5, -3]

print(sumOfSubArray(numbers))

# ----------------------------------------------------------

# 2ND APPROACH
# when negative values are not considered


def sumOfSubArray2(numbers):
    current = 0
    maxSoFar = 0
    for number in numbers:
        current += number
        if current < 0:
            current = 0
        if current > maxSoFar:
            maxSoFar = current
    return maxSoFar


print(sumOfSubArray2(numbers))

# ----------------------------------------------------------

# 3RD APPROACH
# when all numbers of the array are negative


def sumOfSubArray3(numbers):
    # initializing the variable with the element of 1st index
    current = numbers[0]
    # initializing the variable with the element of 1st index
    maxTillNow = numbers[0]

    # running a for loop from 2nd index
    for index in range(1, len(numbers)):
        # keeping the maximum value between current element and sum of previous elements
        current = max(numbers[index], numbers[index]+current)
        # keeping the maximum value between current sum of elements and previous sum of elements
        maxTillNow = max(maxTillNow, current)

    return maxTillNow  # returning the maximum value


print(sumOfSubArray3(numbers))
