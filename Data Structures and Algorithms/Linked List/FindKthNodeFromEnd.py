# Instructions:
# LL: Find Kth Node From End (âš¡Interview Question)
# Method name:
# find_kth_from_end

# Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

# For example, let's say you want to find the item that is 3 steps away from the end of the LL. To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.

# This is the problem of finding the "kth node from the end" of a linked list. Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list. If the linked list has fewer than k items, the program should return None.

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

# optimized solution:
def find_kth_from_end_without_length(head, index):
    slow = fast = head

    for _ in range(index):
        if fast is None:
            return None
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow


def find_kth_from_end(head, index):
    if index < 0:
        return None
    
    temp = head
    temp_index = -1

    while temp:
        temp = temp.next
        temp_index+=1

    if index > temp_index:
        return None
    
    length = temp_index - index

    temp = head
    for _ in range(length):
        temp = temp.next
    
    return temp

ll = LinkedList(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
print()
# print(find_kth_from_end(ll.head, -1))
print(find_kth_from_end_without_length(ll.head, 3).value)