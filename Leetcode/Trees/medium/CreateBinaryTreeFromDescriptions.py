# 2196. Create Binary Tree From Descriptions

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Example 1:
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

# Example 2:
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
 
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        allNodes = {}
        chilren = set()

        for parent, child, isLeft in descriptions:
            chilren.add(child)

            if parent not in allNodes:
                allNodes[parent] = TreeNode(parent)
            if child not in allNodes:
                allNodes[child] = TreeNode(child)
            if isLeft:
                allNodes[parent].left = allNodes[child]
            else:
                allNodes[parent].right = allNodes[child]
        
        for parent, child, isLeft in descriptions:
            if parent not in chilren:
                return allNodes[parent]