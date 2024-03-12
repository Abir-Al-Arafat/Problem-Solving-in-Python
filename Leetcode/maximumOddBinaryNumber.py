# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.

 

# Example 1:

# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
# Example 2:

# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeroes = ones =""
        res = ""
        for zero in s:
            if zero == '0':
                zeroes+=zero
        for one in s:
            if one == '1':
                ones += one
        if len(ones) == 1:
            res+=zeroes
            res+=ones
        else:
            count = len(ones)
            for idx in range(count-1):
                res+=ones[idx]
            res+=zeroes
            res+=ones[0]
        
        return res
    
    def maximumOddBinaryNumber2(self, s: str) -> str:
        count = 0
        for number in s:
            if number == "1":
                count += 1
        
        return (count-1) * "1" + (len(s) - count) * "0" + "1" 
    
    def maximumOddBinaryNumber3(self, s: str) -> str:
        s = [n for n in s]
        left = 0

        for idx in range(len(s)):
            if s[idx]=="1":
                temp = s[idx]
                s[idx] = s[left]
                s[left] = temp
                left += 1
        
        temp = s[left-1]
        s[left-1] = s[len(s)-1]
        s[len(s)-1] = temp

        return "".join(s)
