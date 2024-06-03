# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        trav = [root]
        result = [root.val]

        while trav:
            travLength = len(trav)
            children = None
            for _ in range(travLength):
                temp = trav.pop(0)

                if temp.left:
                    children = temp.left.val
                    trav.append(temp.left)
                if temp.right:
                    children = temp.right.val
                    trav.append(temp.right)
            if children:
                result.append(children)
        
        return result
    
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        trav = [root]
        result = [root.val]

        while trav:
            travLength = len(trav)
            children = None
            for _ in range(travLength):
                temp = trav.pop(0)
                print("temp", temp.val)
                print("temp left", temp.left)
                print("temp right", temp.right)

                if temp.left:
                    children = temp.left.val
                    trav.append(temp.left)
                if temp.right:
                    children = temp.right.val
                    trav.append(temp.right)
                print("children", children)
            print("---------------")
            print("children", children)
            if children is not None:
                result.append(children)
        
        return result

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(0)

print(head.val)
print(head.left.val)
print(head.right.val)

solulu = Solution()
print(solulu.rightSideView2(head))