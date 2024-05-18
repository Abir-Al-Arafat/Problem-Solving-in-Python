# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def generate(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            
            if open<n:
                stack.append("(")
                generate(open+1, close)
                stack.pop()
            
            if close<open:
                stack.append(")")
                generate(open, close+1)
                stack.pop()

        generate(0, 0)

        return result

solulu = Solution()

print(solulu.generateParenthesis(2))