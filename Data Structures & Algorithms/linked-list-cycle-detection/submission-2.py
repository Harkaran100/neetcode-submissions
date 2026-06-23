# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a set to store every node we visit
        # do this while current so can go through whole linked list
        # if current.next in set return true else outside of while loop return false

        visited = set() # space o(n)
        current = head
        while current:
            # check if current in hashset
            if current in visited:
                return True
            else:
                visited.add(current) # add to visited
                current = current.next # move current
        return False
            
                
        