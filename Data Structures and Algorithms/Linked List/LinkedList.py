# implement a linked list
# there will be two classes 'Node' and 'LinkedList'
# 'Node' class will be responsible for creating nodes
# 'LinkedList' class will be resposnible for creating linked lists

# node class for initializing nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class for creating linked list


class LinkedList:
    def __init__(self, value):
        # using node class to create a new node
        new_node = Node(value)
        # setting head and tail to new node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # method for printing all the nodes

    def print_list(self):
        # keeping the head node in a variable
        temp = self.head
        # running a loop in temp variable
        while temp is not None:
            print(temp.value, end=' ')
            # setting the next pointer as temp value
            temp = temp.next

    # method for adding a node at the end
    def append(self, value):
        # creating node using 'Node' class
        new_node = Node(value)

        # checking if the list is empty or not
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # method for removing a node from the end
    def pop(self):
        # checking if the linked list is empty or not
        if self.length == 0:
            return None

        # keeping the head in two variables to iterate over the list
        temp = self.head
        pre = self.head

        # iterating over the list
        while temp.next:
            pre = temp
            temp = temp.next

        # setting the 2nd last value as tail
        self.tail = pre
        # removing the previous tail
        self.tail.next = None
        # decreasing length
        self.length -= 1

        # checking if the length is 0 again
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    # adding a node to the beginning of the list
    def prepend(self, value):
        # creating node using 'Node' class
        new_node = Node(value)

        # checking if the list is empty or not
        if self.length == 0:
            # setting head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # setting the node's next pointer to previous head
            new_node.next = self.head
            # setting the new node as head
            self.head = new_node
        self.length += 1
        return True

    # method for removing a node from the beginning
    def pop_first(self):
        # checking if the linked list is empty or not
        if self.length == 0:
            return None

        # keeping the head node in a variable
        temp = self.head
        # setting the head value to the next pointer
        self.head = self.head.next
        # disconnecting the previous head node
        temp.next = None
        # decreasing length
        self.length -= 1

        # condition to set the tail node to none
        if self.length == 0:
            self.tail = None

        return temp

    # method for getting a value by index
    # def get(self, index):
    #     if self.length == 0:
    #         return None
    #     if index == 0:
    #         return self.head.value
    #     if index == self.length-1:
    #         return self.tail.value
    #     if 0 < index < self.length:
    #         temp = self.head
    #         count = 0
    #         while count != index:
    #             temp = temp.next
    #             count += 1
    #         return temp.value

    # method for getting a value by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # method for replacing a node in a given index
    def set_value(self, index, value):
        # using get method to get the node
        temp = self.get(index)
        # checking if the variable consists a node or not
        if temp:
            # setting the node's value to new value
            temp.value = value
            return True
        return False

    # method for inserting a node in a given index
    def insert(self, index, value):
        # checking if the index is valid or not
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        # creating new node using node class
        new_node = Node(value)
        # keeping the indexed node's previous node in a variable
        temp = self.get(index-1)
        # setting the new node's next pointer
        new_node.next = temp.next
        # setting the new node in the indexed place
        temp.next = new_node
        self.length += 1
        return True

    # method for removing a node
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        # triggers "pop_first" method if it is the first index
        if index == 0:
            return self.pop_first()
        # triggers "pop" method if it is the last index
        if index == self.length-1:
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next

        # removing the indexed node
        prev.next = temp.next
        # breaking the node off of the list
        temp.next = None
        self.length -= 1
        return temp

    # method for reversing
    def reverse(self):
        # keeping head node in a variable
        temp = self.head
        # keeping tail node in the head node
        self.head = self.tail
        # keeping head node in the tail node
        self.tail = temp

        # second node in a variable
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)

ll.print_list()
print()
ll.reverse()
ll.print_list()
print('\n', ll.head.value)
print(ll.tail.value)
