# implement the stack data structure
# declare a 'Node' class to create node
# declare a 'Stack' class to create the stack
# in the 'Stack' class, implement the following::
# a method named 'push' to add a node at the end
# a method named 'pop' to remove a node from the end

# node class to create node
class Node:
    # constructor to initialize the value and next pointer
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # constructor to initialize the node
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    # method to print the stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # method to add an item
    def push(self, value):
        # creating a new node
        new_node = Node(value)

        if self.length == 0:
            # setting new node as top node if stack is empty
            self.top = new_node
        else:
            # setting the next pointer of new node as top node
            new_node.next = self.top
            # setting new node as top node
            self.top = new_node

        self.length += 1

    # method to remove an item
    def pop(self):
        # checking if the stack has any element
        if self.length == 0:
            return None

        # keeping top element in a variable
        temp = self.top
        # setting top value to next value
        self.top = self.top.next
        # setting the previous top's next pointer to none
        temp.next = None
        self.length -= 1

        return temp


stack = Stack(5)
stack.push(4)
stack.push(3)
stack.print_stack()
print('length: ', stack.length)

print('top:', stack.top.value)

print('popped', stack.pop().value)
stack.print_stack()
print('length: ', stack.length)

print('top:', stack.top.value)

print('popped', stack.pop().value)
stack.print_stack()
print('length: ', stack.length)

print('top:', stack.top.value)

print('popped', stack.pop().value)
stack.print_stack()
print('length: ', stack.length)

print('top:', stack.top)
print('last pop:', stack.pop())
