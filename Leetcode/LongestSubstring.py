# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(string):
    # initializing window and length
    window = []
    length = 0

    # iterating over the string
    for char in string:
        # checking if the character is available inside the window
        if char not in window:
            window.append(char)
        else:
            # removing duplicates
            while char != window[0]:
                window.pop(0)
            window.pop(0)
            # appending new character
            window.append(char)
        # checking if highest length is found
        if len(window) > length:
            length = len(window)
    # returning length
    return length, window


s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
# s = "aab"
print(lengthOfLongestSubstring(s))
