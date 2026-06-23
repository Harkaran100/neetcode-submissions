# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## turn this into two lists
        # everything upuntil half is first list
        # everything half to the end is another list
        # reverse the second half
        # merge the 2 sorted lists
        # how to get to half of linked list?

        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is now the half way point
        halfway = slow

        # reverse  from slow + 1 to fast
        # but ensure fast isnt out of bounds, how
        prev = None
        curr = slow.next
        slow.next = None # disconnect
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # by this point the entire linked list is same first half second half reversed.
        # first half linked list is started from head, second half from prev, its 2 linked lists now
        first = head
        second = prev

        while first and second:

            # get next before disconnect
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        