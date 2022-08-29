# implement the queue data structure
# declare a 'Node' class to create node
# declare a 'Queue' class to create the Queue
# in the 'Queue' class, implement the following::
# a method named 'enqueue' to add a node at the end
# a method named 'dequeue' to remove a node from the beginning

# node class to create node

class Node:
    # constructor to initialize the value and next pointer
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    # constructor to initialize the node
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # method to print the stack
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    # method to add an item to the end
    def enqueue(self, value):
        # creating a new node
        new_node = Node(value)
        if self.first is None:
            # setting new node as first and last node if queue is empty
            self.first = new_node
            self.last = new_node
        else:
            # setting last node's next node as new node
            self.last.next = new_node
            # setting new node as last node
            self.last = new_node

        self.length += 1
        return True

    # method to remove an item from the beginning
    def dequeue(self):
        # checking if there is any item
        if self.length == 0:
            return None
        # keeping first node in a temp variable
        temp = self.first
        if self.length == 1:
            # setting first and last node to none
            self.first = None
            self.last = None
        else:
            # pointing first node to the next node
            self.first = self.first.next
            # disconnecting the first node
            temp.next = None

        self.length -= 1
        return temp


queue = Queue(3)
print('first:', queue.first.value)
print('last:', queue.last.value)
print('length:', queue.length)
queue.print_queue()

print()
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(0)
queue.print_queue()
print('first:', queue.first.value)
print('last:', queue.last.value)
print('length:', queue.length)
queue.print_queue()
print()
print("------dequeue------")
print("dequeue", queue.dequeue().value)
queue.print_queue()
print('first:', queue.first.value)
print('last:', queue.last.value)
print('length:', queue.length)

print("dequeue", queue.dequeue().value)
queue.print_queue()
print('first:', queue.first.value)
print('last:', queue.last.value)
print('length:', queue.length)

queue.dequeue()
queue.print_queue()
print('first:', queue.first.value)
print('last:', queue.last.value)
print('length:', queue.length)

queue.dequeue()
queue.print_queue()
print('first:', queue.first)
print('last:', queue.last)
print('length:', queue.length)
