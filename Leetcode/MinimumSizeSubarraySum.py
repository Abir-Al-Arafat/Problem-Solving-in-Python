# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

def minSubArrayLen(target, nums):
    # for keeping sub array
    window = []
    # for calculating sum
    sum = 0
    # for keeping length
    length = 0
    # for keeping minimum length
    finalLength = float('inf')
    # left pointer
    left = 0

    for right in range(len(nums)):
        # adding elements
        window.append(nums[right])
        # adding values
        sum += nums[right]

        # loop runs till the sum is greater or equal to target
        while sum >= target:
            # print(window)
            # keeping length
            length = len(window)
            # checking if a minmum length is found
            if length < finalLength:
                finalLength = length
                # print(finalLength)
            # deducting
            sum -= nums[left]
            # removing first element from window
            window.pop(0)
            # shifting pointer
            left += 1
    # returns 0 if a minimum length is not found
    if finalLength == float('inf'):
        return 0
    # returns minimum length
    return finalLength


target = 15
nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
print(minSubArrayLen(target, nums))
