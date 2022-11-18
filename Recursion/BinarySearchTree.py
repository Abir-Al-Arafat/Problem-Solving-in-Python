# implement a binary search tree
# define a class which makes a node
# define a function which adds a node to a tree using recursion
# define a function which removes a node from a tree using recursion
# define a function which can search a value in a tree using recursion
# define a function which can find the lowest valued node from the tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# function to search a node
# takes two parameters, the root and the value that needs to be found


def search(root, target):
    if not root:
        return False

    if target > root.value:
        return search(root.right, target)
    elif target < root.value:
        return search(root.left, target)
    else:
        return True

# function to insert a node
# takes two parameters, the root and the node that needs to be inserted


def insert(root, value):
    if not root:
        return Node(value)

    if value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)
    return root

# function to find the lowest valued node from a tree


def minNode(root):
    temp = root
    while temp and temp.left:
        temp = temp.left

    return temp


node = Node(5)
node4 = Node(4)
node6 = Node(6)
node.left = node4
node.right = node6
print(" ", node.value)
print(node.left.value, " ", node.right.value)

print(insert(node, 7).value)
print(insert(node, 3).value)
print(node.left.left.value)
print(minNode(node).value)
