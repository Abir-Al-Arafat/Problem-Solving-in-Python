# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# method - 1
# O(n^2)
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True

    return False

# method - 2
# O(n)


def containsNearbyDuplicate2(nums, k):
    window = []

    for val in nums:
        if val in window:
            return True
        window.append(val)
        if len(window) > k:
            window.pop(0)

    return False
# method - 3
# O(n)


def containsNearbyDuplicate3(nums, k):
    left = 0
    window = []

    for right in range(len(nums)):
        if (right - left) > k:
            window.pop(0)
            left += 1

        if nums[right] in window:
            return True

        window.append(nums[right])

    return False

# method - 4 (Using set)
# O(n)


def containsNearbyDuplicate4(nums, k):
    # initializing set
    window = set()
    # setting left pointer to 0
    left = 0

    for right in range(len(nums)):
        # checking if the window exceeds the limit
        if right - left > k:
            # removing item from left
            window.remove(nums[left])
            # increasing left index
            left += 1
        # checking if the value exists
        if nums[right] in window:
            return True
        # adding value to the window
        window.add(nums[right])

    return False


nums = [1, 0, 1, 1]
k = 1
print(containsNearbyDuplicate(nums, k))
print(containsNearbyDuplicate2(nums, k))
print(containsNearbyDuplicate3(nums, k))
print(containsNearbyDuplicate4(nums, k))
