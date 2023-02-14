# determine if a linked list has a cycle
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

        # finding the node which is going to be connected
        for _ in range(idx):
            temp = temp.next

        # connecting the node
        self.tail.next = temp

    # method to see if a cycle exists
    # returns true if a cycle exists
    def hasCycle(self):
        # setting up pointers
        slow, fast = self.head, self.head

        # iterating over the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # checking if a cycle exists
            if fast.value == slow.value:
                return True

        return False

    # method to print the linked list values WITHOUT CYCLE
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

# function to print cycled linked list values


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
ll.makeCycle(4)
print("Has Cycle:", ll.hasCycle())
# print(ll.head.next.next.next.next.next.value)
print_list(ll.head, 20)
