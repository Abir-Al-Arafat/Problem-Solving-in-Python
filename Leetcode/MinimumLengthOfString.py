# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

# Example 1:

# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.

# Example 2:
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".

# Example 3:
# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

string = "aabccabba"

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0 
        right = len(s)-1
        while left < right and s[left] == s[right]:
            temp = s[left]
            while left<=right and s[left] == temp:
                left+=1
            while left<=right and s[right] == temp:
                right-=1
        return (right-left+1)
s = Solution()
print(s.minimumLength(string))