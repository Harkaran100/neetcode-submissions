# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyStartNode = ListNode()
        current = dummyStartNode
        while list1 and list2: # add lower value while both lists
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #when 1 list is done add all of others remaining
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummyStartNode.next
