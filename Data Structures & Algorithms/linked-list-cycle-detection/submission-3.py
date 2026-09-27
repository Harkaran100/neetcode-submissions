# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        tail = head
        while tail: #not none
            if tail in hashset:
                return True
            hashset.add(tail)
            tail = tail.next
        return False