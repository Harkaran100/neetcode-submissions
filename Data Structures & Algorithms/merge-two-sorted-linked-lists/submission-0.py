# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if not list1:
            tail.next = list2
        elif not list2:
            tail.next = list1
        return dummyNode.next

        
        # compare head of both lists, which ever is smaller gets posotion 1 
        # in joined array, the larger one gets compared to the other indexs 
        # second index, which ever is smaller gets added to position 2 then 
        # the larger one in comparision is compared to the opposite linked 
        # lists next index, this process is repeated until current.next is null for the opposite linked list
        # then all remaining index in current linked list are appeneded at end 