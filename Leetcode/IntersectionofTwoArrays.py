# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# res = []

# for value in nums1:
#     if value not in res and value in nums2:
#         res.append(value)

# for value in nums2:
#     if value not in res and value in nums1:
#         res.append(value)



# print(res)

class Solution:
    def intersection(self, nums1, nums2):
        exists = set(nums1)
        res = []

        for value in nums2:
            if value in exists:
                res.append(value)
                exists.remove(value)
        
        return res
    
solution = Solution()
print(solution.intersection(nums1, nums2))