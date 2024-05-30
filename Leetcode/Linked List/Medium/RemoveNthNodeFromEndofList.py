# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

from MergeInBetweenLinkedLists import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while temp: 
            temp = temp.next
            count += 1
        
        if count == 1:
            head = None
            return head
        
        limit = count - n
        if limit == 0:
            prev = head
            head = head.next
            prev.next = None
            return head
        curr = head
        prev = curr
        for _ in range(limit):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr.next = None

        return head
