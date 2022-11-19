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

# function to remove a node from a tree


def remove(root, target):
    if not root:
        return None

    if target > root.value:
        root.right = remove(root.right, target)
    elif target < root.value:
        root.left = remove(root.left, target)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = minNode(root.right)
            root.value = min_node.value
            root.right = remove(root.right, min_node.value)
    return root

# function for inorder traversal


def dfs_inorder(root):
    temp = root

    if temp and temp.left:
        dfs_inorder(root.left)

    print(temp.value, end=" ")
    if temp and temp.right:
        dfs_inorder(root.right)

# function for preorder traversal


def dfs_preorder(root):
    temp = root

    print(temp.value, end=" ")
    if temp and temp.left:
        dfs_preorder(temp.left)
    if temp and temp.right:
        dfs_preorder(temp.right)

# function for postorder traversal


def dfs_postorder(root):
    temp = root

    if temp and temp.left:
        dfs_postorder(temp.left)
    if temp and temp.right:
        dfs_postorder(temp.right)
    print(temp.value, end=" ")

# function for printing the tree values in reversed order


def reverse(root):
    temp = root

    if temp and temp.right:
        reverse(root.right)
    print(temp.value, end=" ")
    if temp and temp.left:
        reverse(root.left)

# function for bfs traversal


def bfs(root):

    if not root:
        return None

    temp = root
    nodes = []
    nodes.append(temp)
    values = []
    values.append(temp.value)

    # if root and root.left:
    #     nodes.append(root.left)
    # if root and root.right:
    #     nodes.append(root.right)

    while nodes:
        node = nodes.pop(0)
        if node.left:
            values.append(node.left.value)
            nodes.append(node.left)
        if node.right:
            values.append(node.right.value)
            nodes.append(node.right)
    return values


node = Node(5)
node4 = Node(4)
node6 = Node(6)
node.left = node4
node.right = node6
print(" ", node.value)
print(node.left.value, " ", node.right.value)

print(insert(node, 7))
print(insert(node, 3))

print("   ", node.value)
print(" ", node.left.value, "  ", node.right.value)
print(node.left.left.value, "       ", node.right.right.value)
# remove(node, 3)
# remove(node, 7)

# print("   ", node.value)
# print(" ", node.left.value, "  ", node.right.value)
# print(node.left.left.value, "       ", node.right.right.value)

# dfs_inorder(node)
# print()
# dfs_preorder(node)
# print()
# dfs_postorder(node)
# print()
# reverse(node)
print(bfs(node))
