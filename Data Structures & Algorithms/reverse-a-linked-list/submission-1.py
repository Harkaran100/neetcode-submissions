# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next # hold the value of next before breaking link
            current.next = prev # break chain and reverse
            prev = current # mpve prev up
            current = next_node # move current up using stored address
        return prev