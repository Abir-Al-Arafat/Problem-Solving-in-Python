# <-- Complicated Problem -->

# determine if a linked list has a cycle and return the head of that cycle
# head of the cycle: head of the cycle is where the cycle starts from
# Time: O(n) Space: O(1)
# class for creating node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    # method for adding an element at the end
    def add_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    # method to make a cycle
    # takes an index as an argument and connects the tail to the indexed node
    def makeCycle(self, idx):
        temp = self.head

        # finding the node which is going to get connected
        for _ in range(idx):
            temp = temp.next

        # connecting the node
        self.tail.next = temp

    # method to see if a cycle exists
    # returns head of the cycle if a cycle exists
    def hasCycleHead(self):
        # setting up pointers
        slow, fast = self.head, self.head

        # iterating over the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # checking if a cycle exists
            if fast.value == slow.value:
                break

        # checking if a cycle doesnt exist
        if not fast or not fast.next:
            return None

        # setting another pointer to find out the cycle head
        slowest = self.head

        # loop runs until the head is found
        while slow.value != slowest.value:
            slow = slow.next
            slowest = slowest.next

        # returns the head of the cycle
        return slowest

    # method to print the linked list values WITHOUT CYCLE
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

# function to print cycled linked list values
# takes two arguments
# a head node and a length to which the cycle is going to be printed


def print_list(head, length):
    temp = head

    for _ in range(length):
        print(temp.value, end=" ")
        temp = temp.next


ll = LinkedList(1)
ll.add_end(2)
ll.add_end(3)
ll.add_end(4)
ll.add_end(5)
# ll.print_list()

# making a cycle at 3rd node
ll.makeCycle(2)
# returning the cycle head
print("Cycle Head:", ll.hasCycleHead().value)
# printing the whole cycle
print_list(ll.head, 20)
