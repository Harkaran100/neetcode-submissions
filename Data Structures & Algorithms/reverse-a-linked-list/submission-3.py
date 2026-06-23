# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # at start its none
        current = head
        while current:
            nextNode = current.next # save next
            current.next = prev
            prev = current
            current = nextNode
        return prev

        
