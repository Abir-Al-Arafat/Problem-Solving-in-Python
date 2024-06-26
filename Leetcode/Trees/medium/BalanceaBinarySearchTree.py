# 1382. Balance a Binary Search Tree
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Example 1:
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# Example 2:
# Input: root = [2,1,3]
# Output: [2,1,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        result = []
        def dfsInOrderTraverse(current_node):
            nonlocal result
            if current_node.left is not None:
                dfsInOrderTraverse(current_node.left)
            result.append(current_node.val)
            if current_node.right is not None:
                dfsInOrderTraverse(current_node.right)
        dfsInOrderTraverse(root)

        def convertToBST(left, right):
            if left>right:
                return None
            
            mid = (left+right)//2
            root = TreeNode(result[mid])
            root.left = convertToBST(left, mid-1)
            root.right = convertToBST(mid+1, right)

            return root
        
        return convertToBST(0, len(result)-1)