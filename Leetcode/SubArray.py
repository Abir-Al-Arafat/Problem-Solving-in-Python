# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


# time complexity: O(n)

# sliding window technique
def numOfSubarrays(arr, k, threshold):
    # initializing
    window = list()
    # setting pointer
    left = 0
    # setting total of elements inside the window
    total = 0
    # setting number of sub arrays
    count = 0

    for right in range(len(arr)):
        # checking if the window exceeds length
        if (right - left) + 1 > k:
            # subtracting first element
            total -= arr[left]
            # removing first element from window
            window.pop(0)
            # shifting pointer
            left += 1
        # adding element to window
        window.append(arr[right])
        # adding total values
        total += arr[right]
        # checking if the window reached desired length
        if len(window) == k:
            # checking average threshold
            if (total / k) >= threshold:
                count += 1

    return count


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

print(numOfSubarrays(arr, k, threshold))
