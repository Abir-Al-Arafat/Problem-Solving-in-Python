# Instructions:
# LL: Reverse Between (⚡Interview Question)
# You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

# Input

# The method reverse_between takes two integer inputs m and n.

# The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)

# Output

# The method should modify the linked list in-place by reversing the nodes from index m to index n.

# If the linked list is empty or has only one node, the method should return None.

# Example

# Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

# Constraints

# The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)

        if self.head and self.tail.next == None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length+=1
        return True
    
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        return self.head
    
    # my solution
    def reverse_between(self, start_idx, finish_idx):
        # checking for valid index
        if not self.head or self.length == 1 or start_idx == finish_idx or start_idx<0 or finish_idx<0 or finish_idx>=self.length or start_idx>finish_idx:
            return None
        
        # initializing
        start_node = end_node = before = self.head

        # these loops are used to store start and end nodes
        # loop for storing start node and the node before start node
        for _ in range(start_idx):
            before = start_node
            start_node = start_node.next
        
        # for storing last node
        for _ in range(finish_idx):
            end_node = end_node.next

        # for storing the node after last node
        end_node_after = end_node.next

        # replacing first and last node (head and tail)
        temp = start_node
        start_node = end_node
        end_node = temp

        # initializing
        temp_before = None
        temp_after = temp.next
        
        # loop for reversing the nodes
        for _ in range((finish_idx-start_idx)+1):
            temp_after = temp.next
            temp.next = temp_before
            temp_before = temp
            temp = temp_after
        
        # checking if head node has changed its position
        if start_idx != 0:
            # setting the next pointer to the reversed nodes
            before.next = temp_before
        else:
            # setting new head node
            self.head = temp_before
        
        # connecting last node to the rest of the nodes
        end_node.next = end_node_after

        # checking if tail pointer needs to get changed
        if end_node_after is None:
            # setting the tail pointer
            self.tail = end_node
        # return temp_before, before, end_node
        return self.head
    # less code optimised solution
    def reverse_between_optimised(self, m, n):
        if not self.head:
            return None
 
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        for i in range(m):
            prev = prev.next
 
        current = prev.next
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
 
        self.head = dummy.next

        return self.head

    
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print_list()
print()
nodes = ll.reverse_between(2, 4)
print("nodes", nodes)
# ll.print_list()

while nodes:
    print(nodes.value, end=" -> ")
    nodes = nodes.next
print()
ll.print_list()
print()
print("head", ll.head.value)
print("tail", ll.tail.value)

# print(nodes[0].value)
# print(nodes[0].next.value)
# print(nodes[0].next.next.value)
# print(nodes[0].next.next.next.value)
# print(nodes[0].next.next.next.next.value)
# print(nodes[1].value)
# print(nodes[1].next.value)
# print("end_node", nodes[2].value)
    
# for _ in range(0):
#     print("printing for range 0")

# head = ll.reverse_between_optimised(0, 4)

# print("optimised")
# while head:
#     print(head.value, end=" -> ")
#     head = head.next