# 424. Longest Repeating Character Replacement(Medium)

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

def characterReplacement(s, k):
    # for characters and number of times it occured
    count = {}
    # longest time a character has occured
    longestFreq = 0
    # for the length of the longest repeating character substring
    output = 0
    # left pointer
    left = 0

    # running for loop on the string
    for right in range(len(s)):
        # checking if the character already exist or not
        if s[right] not in count:
            # adding number of ouccurences of the character
            count[s[right]] = 1
        else:
            # adding number of ouccurences of the character
            count[s[right]] += 1
        # loop on the occurences
        for char in count:
            # checking the highest time a character has occurred
            if count[char] > longestFreq:
                longestFreq = count[char]

        # checking if a valid window exist
        if (right-left+1) - longestFreq <= k:
            # setting the length of the longest repeating characters
            output = (right-left+1)
        else:
            # subtracting occurrence when valid window doesnt exist
            count[s[left]] -= 1
            # increasing pointer
            left += 1
    # returning length
    return output


s = "ABAB"
k = 2

s = "AABABBA"
k = 1
print(characterReplacement(s, k))
