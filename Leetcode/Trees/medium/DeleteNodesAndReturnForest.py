# 1110. Delete Nodes And Return Forest

# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Example 1:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# Example 2:
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        result = set([root])

        def dfs(root):
            if not root:
                return None
            node = root
            if root.val in to_delete:
                node = None
                result.discard(root)
                if root.right:
                    result.add(root.right)
                if root.left:
                    result.add(root.left)
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            return node
        dfs(root)

        return list(result)
        # return result
    
solulu = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print(solulu.delNodes(root, to_delete=[3,5]))

# print(set([root]))