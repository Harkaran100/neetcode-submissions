# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass purpose to count size of linked list
        total_size = 0
        curr = head
        while curr:
            curr = curr.next
            total_size += 1
        
        # 1st index based
        removeIndex = total_size - n

        if removeIndex == 0:
            return head.next

        # 2nd pass 
        curr = head
        currSize = 0
        while curr:
            if currSize == (removeIndex - 1): # Index prior
                curr.next = curr.next.next
                currSize += 1
            else:
                curr = curr.next
                currSize += 1
        return head




        # 2 pass first pass to get len of entire linked list
        # then do linked list len - n
        # tells us which needs to be removed
        # do second pass keep track of where we are
        # once at the value at value before do current.next = current.next.next
        # then keep going
        