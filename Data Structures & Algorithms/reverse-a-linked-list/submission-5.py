# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is beggining
        # can be done in On time via traversing and changing 1 link at a time
        current = head
        prev = None
        while current:
            nextNode = current.next # saved before breaking link
            current.next = prev
            prev = current
            current = nextNode
        return prev

            # example [3 --> 2 --> 1 --> 0]
            # [ <--3  2 --> 1 --> 0]
            # [ <--3  2 --> 1 --> 0]

        