# implement a binary search tree
# define a 'Node' class to create node
# define a 'BinarySearchTree' class to do the following
# define a constructor which sets the root node to 'None'
# define an 'insert' method to insert a node into the binary search tree
# define a 'contains' method which checks if a node exists into a binary search tree
# define a 'dfs_pre_order' method which traverses the tree using depth first search pre order technique
# define a 'dfs_post_order' method which traverses the tree using depth first search post order technique
# define a 'dfs_in_order' method which traverses the tree using depth first search in order technique

# class to create a node

class Node:
    # constructor to initialize the value and left and right pointer
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# class to create a tree


class BinarySearchTree:
    # constructor to initialize the root
    def __init__(self):
        # setting root node to none
        self.root = None

    # method to add a node
    def insert(self, value):
        # creating new node
        new_node = Node(value)

        # checking if the root node is none
        if self.root is None:
            # setting the new node as root node
            self.root = new_node
            return True

        # keeping the root node in a variable
        temp = self.root
        while (True):
            # checking if the tree already has a similar node or not
            if temp.value == new_node.value:
                return False

            # if the value of the inserted node is bigger than the root node, then it will go to right child
            if new_node.value > temp.value:
                if temp.right is None:
                    # if right child is none then it will be set to new node
                    temp.right = new_node
                    return True
                # if right child has a value then temp variable will move right
                temp = temp.right

            # if the value of the inserted node is smaller than root node, then it will go to left child
            else:
                if temp.left is None:
                    # if left pointer is none then it will be set to new node
                    temp.left = new_node
                    return True
                # if left child has a value then temp variable will move left
                temp = temp.left

    # method to search a node:
    def contains(self, value):
        # checking if there any node exists or not
        if self.root is None:
            return False

        # keeping the root node in a variable
        temp = self.root

        # loop runs unless a none value found
        while temp is not None:
            # checking if the value is greater than root node or not
            if value > temp.value:
                # temp variable goes to right part of the tree if the value is greater than a node
                temp = temp.right
            # checking if the value is less than root node or not
            elif value < temp.value:
                # temp variable goes to left part of the tree if the value is less than a node
                temp = temp.left
            else:
                # returns true if the value is equal to a node
                return True

        return False

    # method to visit all the nodes
    def dfs_pre_order(self):
        # list to keep the traversed nodes
        result = []

        # method to visit all the nodes in pre order
        def traverse(current_node):
            # appending the value of current node
            result.append(current_node.value)

            # checking if the left child exists
            if current_node.left is not None:
                # visiting left child
                traverse(current_node.left)

            # checking if the right child exists
            if current_node.right is not None:
                # visiting right child
                traverse(current_node.right)

        # using root node as argument because the traversing will start from the root
        traverse(self.root)
        return result

    # method to visit all the nodes
    def dfs_post_order(self):
        # list to keep the traversed nodes
        result = []

        # method to visit all the nodes in post order
        def traverse(current_node):
            # checking if the left child exists
            if current_node.left is not None:
                # visiting left child
                traverse(current_node.left)

            # checking if the right child exists
            if current_node.right is not None:
                # visiting right child
                traverse(current_node.right)
            # appending the value of current node
            result.append(current_node.value)
        # using root node as argument because the traversing will start from the root
        traverse(self.root)
        return result

    # method to visit all the nodes
    def dfs_in_order(self):
        # list to keep the traversed nodes
        result = []

        # method to visit all the nodes in in_order
        def traverse(current_node):
            # checking if the left child exists
            if current_node.left is not None:
                # visiting left child
                traverse(current_node.left)

            # appending the value of current node
            result.append(current_node.value)

            # checking if the right child exists
            if current_node.right is not None:
                # visiting right child
                traverse(current_node.right)
        # using root node as argument because the traversing will start from the root
        traverse(self.root)
        return result


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
print("root node:", bst.root.value)
print("right node:", bst.root.right.value)
print("left node:", bst.root.left.value)

print(bst.contains(47))

print("DFS Pre Order", bst.dfs_pre_order())
print("DFS Post Order", bst.dfs_post_order())
print("DFS In Order", bst.dfs_in_order())
