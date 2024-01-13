# Instructions:
# LL: Remove Duplicates (⚡Interview Question)
# You are given a singly linked list that contains integer values, where some of these values may be duplicated.

# Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

# Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

# You can implement the remove_duplicates() method in two different ways:

# Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

# Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.

# Here is the method signature you need to implement:

# def remove_duplicates(self):

# Example:

# Input:

# LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

# Output:

# LinkedList: 1 -> 2 -> 3 -> 4 -> 5

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

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=' ')
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length+=1
        return True

# O(n^2)
def remove_duplicates(head):
    temp = head
    temp_nested = head

    while temp:
        while temp_nested.next:
            # if temp_nested.next:
            if temp.value == temp_nested.next.value:
                removed_node = temp_nested.next
                temp_nested.next = temp_nested.next.next
                removed_node.next = None
            temp_nested = temp_nested.next
        
        temp_nested = temp.next
        temp = temp.next
    
    return head

# O(n) Optimal
def remove_duplicates_using_sets(head):
    values = set()
    prev = head
    current = head

    while current:
        if current.value in values:
            remove_node = current
            prev.next = current.next
            remove_node.next = None
        else:
            values.add(current.value)
            prev = current
        current = current.next
    
    return head

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(5)
ll.print_list()
print()
# print(ll.head.value)
# print(ll.tail.value)

remove_duplicated_ll = remove_duplicates(ll.head)
remove_duplicated_using_sets_ll = remove_duplicates_using_sets(ll.head)

print("remove_duplicated_ll", remove_duplicated_ll)
print("remove_duplicated_using_sets_ll", remove_duplicated_using_sets_ll)


while remove_duplicated_ll:
    print(remove_duplicated_ll.value, end=' ')
    remove_duplicated_ll = remove_duplicated_ll.next

print()
print("Using Sets (more optimised 0(n)):")
while remove_duplicated_using_sets_ll:
    print(remove_duplicated_using_sets_ll.value, end=" ")
    remove_duplicated_using_sets_ll = remove_duplicated_using_sets_ll.next