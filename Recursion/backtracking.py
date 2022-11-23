# write a function to determine if a path exists from the root of the tree to a leaf node. it may not contain any zeroes

# write a function to determine if a path exists from the root of the tree to a leaf node. it may not contain any zeroes and it should keep the non-zero nodes of the existed path inside of a list and returns the list

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# function to determine if a non-zero path exists


def nonZeroPath(root):
    if not root or root.value == 0:
        return False

    if not root.left or not root.right:
        return True

    if nonZeroPath(root.left):
        return True

    if nonZeroPath(root.right):
        return True

    return False

# function to determine if a non-zero path exists and return the nodes


def nonZeroPathNodes(root, path):
    if not root or root.value == 0:
        return None
    path.append(root.value)

    if not root.left and not root.right:
        return path

    if nonZeroPathNodes(root.left, path):
        return path

    if nonZeroPathNodes(root.right, path):
        return path

    path.pop()
    return


root_node = Node(4)
node0 = Node(0)
node1 = Node(1)
node7 = Node(7)
node2 = Node(2)
#
node3 = Node(3)

root_node.left = node0
root_node.right = node1

root_node.left.right = node7
# root_node.right.left = node2
# root_node.right.right = node0

#
root_node.right.left = node3
root_node.right.left.right = node0
root_node.right.right = node2

# level - 1
print("     ", root_node.value)

# level - 2
print("  ", root_node.left.value, "    ", root_node.right.value)

# level - 3
# print("    ", root_node.left.right.value, "",
#       root_node.right.left.value, " ", root_node.right.right.value)

# level - 3
print("    ", root_node.left.right.value, "",
      root_node.right.left.value, " ", root_node.right.right.value)
# level - 4
print("         ", root_node.right.left.right.value)

print(nonZeroPath(root_node))
print(nonZeroPathNodes(root_node, []))
