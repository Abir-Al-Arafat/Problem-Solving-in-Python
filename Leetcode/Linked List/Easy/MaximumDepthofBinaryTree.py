# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# method to visit all the nodes
def dfs_pre_order(root):
    result = []
    # method to visit all the nodes in pre order
    def traverse(current_node):
        # appending the value of current node
        result.append(current_node.val)

        # checking if the left child exists
        if current_node.left is not None:
            # visiting left child
            traverse(current_node.left)

        # checking if the right child exists
        if current_node.right is not None:
            # visiting right child
            traverse(current_node.right)
    traverse(root)
    return result

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        output = 1
        increment = 1

        def trav(root):
            nonlocal increment
            nonlocal output
            if root.left:
                increment+=1
                output = max(output, increment)
                trav(root.left)
            if root.right:
                increment+=1
                output = max(output, increment)
                trav(root.right)
            increment -= 1
        trav(root)
        return output
    
    #solution 2
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    #solution - 3 using bfs
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level
    
    # solution - 4 using Iterative DFS
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [[root, 1]]
        level = 0

        while queue:
            node, depth = queue.pop()
            if node:
                level = max(level, depth)
                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])
        return level

solulu = Solution()

print(dfs_pre_order(root))
print(solulu.maxDepth(root))