# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # them being in reverse helps us makes it easy can add each value
        # also need to have a carry value
        # edge cases to worry about  
        # [6] [9 1] = [9 7] edge case as second link created in val but not in either link list
        
        dummyNode = ListNode() # creates new link list
        curr = dummyNode
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            value = val1 + val2 + carry # carry from before aswell

            carry = (value) // 10
            value = (value) % 10

            curr.next = ListNode(value)
            curr = curr.next
            if l1:
                l1 = l1.next # move forward 
            if l2:
                l2 = l2.next # move forward
        return dummyNode.next
