# Find the middle node of a linked list with two pointers
# Time Complexity: O(n), Space: O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def addend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

# function to find the middle node of the linked list


def middleNode(head):
    # using two pointers to find the middle node
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


ll = LinkedList(1)
ll.addend(2)
ll.addend(3)
ll.addend(4)
ll.addend(5)
# ll.addend(6)
print(ll.head.value)
print(ll.tail.value)
ll.print_list()
print()
print(middleNode(ll.head).value)
