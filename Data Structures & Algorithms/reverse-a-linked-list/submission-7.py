# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next # store next
            curr.next = prev # change link
            prev = curr # move up prev
            curr = nxt # move up curr
        return prev


            #None a -> b
            #save b
            #reverse link from a-> b to b<- a
            #move up curr