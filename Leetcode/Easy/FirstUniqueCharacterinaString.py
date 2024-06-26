# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        for idx, key in enumerate(s):
            if count[key] == 1:
                return idx

        return -1