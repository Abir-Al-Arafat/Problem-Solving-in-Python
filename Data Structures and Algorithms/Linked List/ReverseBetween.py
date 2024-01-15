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

    def reverse_between(self, start_idx, finish_idx):
        if self.head is None or self.length == 1:
            return None
        
        start_node = end_node = before = self.head

        for _ in range(start_idx):
            before = start_node
            start_node = start_node.next
        for _ in range(finish_idx):
            end_node = end_node.next

        end_node_after = end_node.next

        temp = start_node
        start_node = end_node
        end_node = temp

        temp_before = None
        temp_after = temp.next

        # return start_node, end_node, temp

        # while temp.value!=start_node.value:
        #     temp_after = temp.next
        #     temp.next = temp_before
        #     temp_before = temp
        #     temp = temp_after
            # if start_node.value == temp.value:
            #     break
        
        for _ in range((finish_idx-start_idx)+1):
            temp_after = temp.next
            temp.next = temp_before
            temp_before = temp
            temp = temp_after
        if start_idx != 0:
            before.next = temp_before
        end_node.next = end_node_after
        # return temp_before, before, end_node
        return self.head
    
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print_list()
ll.reverse()
print()
ll.print_list()
print()
ll.reverse()
ll.print_list()
print()
nodes = ll.reverse_between(1, 2)

# ll.print_list()

# print("start_node", nodes[0].value)
# print("start_node", nodes[0].next)
# print("end_node", nodes[1].value)
# print("end_node", nodes[1].next)
# print("end_node", nodes[1].next.value)
# print("end_node", nodes[1].next.next.value)
# print("temp (start node)", nodes[2].value)
# print("temp (start node)", nodes[2].next)
# print("temp (start node)", nodes[2].next.value)

# print(nodes.value)
# print(nodes.next.value)
# print(nodes.next.next.value)
# print(nodes.next.next.next)

# print(nodes.value)
# print(nodes.next.value)
# print(nodes.next.next.value)
# print(nodes.next.next.next.value)
# print(nodes.next.next.next.next.value)
while nodes:
    print(nodes.value, end=" -> ")
    nodes = nodes.next
ll.print_list()
# print(nodes[0].value)
# print(nodes[1].value)
# print(nodes[2].next)
    
for _ in range(0):
    print("printing for range 0")