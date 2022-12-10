# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    chars = ''
    for char in s:
        if char.isalpha() or char.isnumeric():
            chars += char
    firstIndex = 0
    lastIndex = len(chars) - 1
    chars = chars.lower()
    while firstIndex < len(chars)//2:
        if chars[firstIndex] == chars[lastIndex]:
            firstIndex += 1
            lastIndex -= 1
        else:
            return False
    return True


s = " "
print(isPalindrome(s))
