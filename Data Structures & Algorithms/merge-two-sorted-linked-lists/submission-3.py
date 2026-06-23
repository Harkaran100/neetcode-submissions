# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # pick smallest of the 2 values
        # then move to next of value picked
        dummyStartNode = ListNode()
        current = dummyStartNode
        while list1 and list2:
            # list 2 has smaller or equal value
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            # list 1 has smaller
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        # when either list is complete

        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummyStartNode.next

        