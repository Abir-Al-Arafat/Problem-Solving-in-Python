# 650. 2 Keys Keyboard

# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

# Example 1:

# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Example 2:

# Input: n = 1
# Output: 0

class Solution:
    def minSteps(self, n: int) -> int:

        def backtrack(count, paste):
            if count == n:
                return 0
            
            if count > n:
                return 1000
            
            # paste
            pasteResult = 1 + backtrack(count+paste, paste)

            # copy paste
            copyPasteResult = 2 + backtrack(count + count, count)

            return min(pasteResult, copyPasteResult)
        
        if n < 2:
            return 0
        
        return 1 + backtrack(1,1)
    # with caching
    def minStepsCaching(self, n: int) -> int:
        cache = {}
        def backtrack(count, paste):
            if count == n:
                return 0
            
            if count > n:
                return 1000

            if (count, paste) in cache:
                return cache[(count, paste)]
            
            # paste
            pasteResult = 1 + backtrack(count+paste, paste)

            # copy paste
            copyPasteResult = 2 + backtrack(count + count, count)

            cache[(count, paste)] = min(pasteResult, copyPasteResult)
            return cache[(count, paste)]
        
        if n < 2:
            return 0
        
        return 1 + backtrack(1,1)

copyPaste = Solution()
copyPaste.minSteps(3)