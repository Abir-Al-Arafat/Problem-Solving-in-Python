# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

def isValid(s):
    stack = []
    values = {")": "(",
              "}": "{",
              "]": "["}

    for brac in s:
        if brac in values:
            if stack and stack[-1] == values[brac]:
                stack.pop()
            else:
                return False
        else:
            stack.append(brac)

    if not stack:
        return True
    else:
        return False


s = "(]"
print(isValid(s))
