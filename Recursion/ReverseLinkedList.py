# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3


def printList(head):
    temp = head

    while temp:
        print(temp.val, end=" ")
        temp = temp.next

# function to reverse linked list iteratively


def reverseList(head):
    temp = head
    before = None

    while temp:
        after = temp.next
        temp.next = before
        before = temp
        temp = after

    return before

# function to reverse linked list recursively


def reverseListRec(head):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseListRec(head.next)
        head.next.next = head
    head.next = None
    return newHead


printList(node1)
print("\nReversed List:")
printList(reverseListRec(node1))
