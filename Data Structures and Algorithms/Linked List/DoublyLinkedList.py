# implement a doubly linked list
# declare a 'Node' class to create node
# declare a 'DoublyLinkedList' class to create the linked list
# 'DoublyLinkedList' class will have a contructor to create a new node which will point to head and tail
# in the 'DoublyLinkedList' class, implement the following
# a method named 'print_list' to print all the nodes
# a method named 'append' to add a node at the end
# a method named 'pop' to remove a node from the end
# a method named 'prepend' to add a node from the beginning
# a method named 'pop_first' to remove a node from the beginning
# a method named 'get' to get a desired node using index number
# a method named 'set_value' to replace a value at the desired node using index number
# a method named 'insert' to insert a node at a desired position using index number
# a method named 'remove' to remove a node from a desired position using index number


# Node class to create node

class Node:
    # initializing a value and two pointers
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        # creating a new node
        new_node = Node(value)
        # setting head and tail
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # method for printing list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    # method for adding a node at the end
    def append(self, value):
        # creating a new node
        new_node = Node(value)

        if self.length == 0:
            # pointing head and tail as the new node if there is no node
            self.head = new_node
            self.tail = new_node
        else:
            # connecting tail to new node
            self.tail.next = new_node
            # connecting new node's previous pointer to tail
            new_node.prev = self.tail
            # setting new node as tail
            self.tail = new_node

        self.length += 1
        return True

    # method to remove a node from the end
    def pop(self):
        # checking if the length is 0 or not
        if self.length == 0:
            return None

        # keeping tail in a variable
        temp = self.tail
        # set head and tail to none if there is only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # taking the tail node one step back
            self.tail = self.tail.prev
            # disconnecting the previous tail node
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    # method to add node in the beginning
    def prepend(self, value):
        # creating a new node
        new_node = Node(value)

        if self.length == 0:
            # pointing head and tail as the new node if there is no node
            self.head = new_node
            self.tail = new_node
        else:
            # pointing head's previous pointer to new node
            self.head.prev = new_node
            # pointing new node's next pointer as head
            new_node.next = self.head
            # setting new node as head
            self.head = new_node
        self.length += 1
        return True

    # method to remove a node from the beginning
    def pop_first(self):
        # checking if the length is 0 or not
        if self.length == 0:
            return None

        # keeping head in a variable
        temp = self.head
        # set head and tail to none if there is only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # taking the head node one step forward
            self.head = self.head.next
            # disconnecting the previous head node
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # method to get a value by index
    def get(self, index):
        # checking validity of index
        if index < 0 or index >= self.length:
            return None

        # checking if the index is close to head or tail
        if index < self.length/2:
            # if the index is close to head, the loop will start from head
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            # if the index is close to tail, the loop will start from tail
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    # method to replace a value by index
    def set_value(self, index, value):
        # getting the node of the index
        temp = self.get(index)

        if temp:
            # setting the node's value to new value
            temp.value = value
            return True
        return False

    # method to insert a node by index
    def insert(self, index, value):
        # checking validity of index
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        # creating a new node
        new_node = Node(value)

        # getting the previous node of indexed node
        before = self.get(index-1)

        # getting the indexed node
        after = before.next

        # setting new node's previous pointer
        new_node.prev = before
        # setting new node's next pointer
        new_node.next = after
        # setting previous node's next pointer to new node
        before.next = new_node
        # setting a node after the new node
        after.prev = new_node

        self.length += 1
        return True

    # method to remove a node by index
    def remove(self, index):
        # checking validity of index
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            # removing node from the beginning
            return self.pop_first()

        if index == self.length-1:
            # removing node from the end
            return self.pop()

        if self.length == 1:
            # keeping head node in a variable
            temp = self.head
            # setting head and tail to none
            self.head = None
            self.tail = None
        else:
            # storing the node before the node which is going to be removed
            before = self.get(index-1)
            # storing the node which is going to be removed
            temp = before.next
            # storing the node after the node which is going to be removed
            after = temp.next

            # joinining the nodes which are before and after the indexed node
            before.next = after
            after.prev = before

            # setting the indexed node's next and previous pointer to null
            temp.next = None
            temp.prev = None

        self.length -= 1

        return temp


dll = DoublyLinkedList(5)
# dll.append(6)
# dll.append(7)
# dll.append(8)
print('length', dll.length, '\n')
dll.print_list()
print()
print(dll.remove(0).value)
dll.print_list()
print('\n length', dll.length, '\n')
# print('\n', dll.length)
