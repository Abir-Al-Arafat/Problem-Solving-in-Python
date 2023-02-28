# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

# idx = 5
# nextEl = (idx + 1) % 4
# print(nextEl)

def maxSubarraySumCircular(nums):
    globalMax = nums[0]
    globalMin = nums[0]
    curMax = 0
    curMin = 0
    total = 0

    for val in nums:
        curMax = max(val, curMax + val)
        curMin = min(val, curMin + val)
        # setting the maximum value
        globalMax = max(curMax, globalMax)
        # setting the minimum value
        globalMin = min(curMin, globalMin)
        # setting the total
        total += val

    # returning the maximum value
    if globalMax < 0:
        return globalMax
    else:
        return max(globalMax, total - globalMin)


nums = [-3, -2, -3]
print(maxSubarraySumCircular(nums))
