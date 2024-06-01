# 102. Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        trav = [root]
        result = [[int(root.val)]]

        while trav:
            travLength = len(trav)
            children = []
            for _ in range(travLength):
                temp = trav.pop(0)

                if temp.left:
                    children.append(int(temp.left.val))
                    trav.append(temp.left)
                if temp.right:
                    children.append(int(temp.right.val))
                    trav.append(temp.right)
            if children:
                result.append(children)
        
        return result