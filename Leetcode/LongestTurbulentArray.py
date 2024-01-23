# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:

# Input: arr = [100]
# Output: 1


def maxTurbulenceSize(arr):
    left = 0
    maxLen = 1
    prev = ""

    for right in range(1, len(arr)):
        if arr[right-1] > arr[right] and prev!=">":
            maxLen = max(maxLen, right - left+1)
            prev = ">"
        elif arr[right-1] < arr[right] and prev != "<":
            maxLen = max(maxLen, right - left + 1)
            prev = "<"
        else:
            if arr[right] == arr[right-1]:
                right = right+1
            left = right - 1
    
    return maxLen

print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(maxTurbulenceSize([4,8,12,16]))
print(maxTurbulenceSize([100]))