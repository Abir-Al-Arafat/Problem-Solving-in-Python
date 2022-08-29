# implement a binary search tree
# define a 'Node' class to create node
# define a 'BinarySearchTree' class to do the following
# define a constructor which sets the root node to 'None'
# define an 'insert' method to insert a node into the binary search tree
# define an 'contains' method which checks if a node exists into a binary search tree


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

            # if the value of the inserted node is bigger than the root node, then it will go to right pointer
            if new_node.value > temp.value:
                if temp.right is None:
                    # if right pointer is none then it will be set to new node
                    temp.right = new_node
                    return True
                # if right pointer has a value then temp variable will move right
                temp = temp.right

            # if the value of the inserted node is smaller than root node, then it will go to left pointer
            else:
                if temp.left is None:
                    # if left pointer is none then it will be set to new node
                    temp.left = new_node
                    return True
                # if left pointer has a value then temp variable will move left
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


bst = BinarySearchTree()
bst.insert(2)
bst.insert(3)
bst.insert(1)
print("root node:", bst.root.value)
print("right node:", bst.root.right.value)
print("left node:", bst.root.left.value)

print(bst.contains(4))
