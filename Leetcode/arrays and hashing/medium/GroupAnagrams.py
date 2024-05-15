# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print(res)
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord("a")] += 1
            res[tuple(count)].append(str)
        return res.values()
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        output = []

        while strs:
            word = strs.pop()
            output.append([word])
            idx = 0
            while idx < len(strs):
                if "".join(sorted(strs[idx])) == "".join(sorted(word)):
                    print("".join(sorted(strs[idx])), "".join(sorted(word)))
                    output[len(output)-1].append(strs[idx])
                    strs.pop(idx)
                    continue
                else:
                    idx+=1
        return output
    
strs = ["eat","tea","tan","ate","nat","bat"]
solulu = Solution()

print(solulu.groupAnagrams2(strs))