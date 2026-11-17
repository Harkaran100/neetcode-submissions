# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head # save the start
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at mid
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # prev is at last value now
        
        while prev:
            if dummy.val == prev.val:
                dummy = dummy.next
                prev = prev.next
            else:
                return False
        return True


        # in even and odd cases first side is shorter or = 

        # plan was to do while dummy I move prev and dummy
        # if disagree false or end return true
        # but dummy will go all the way to end not stop at mid
        # should i instead do while prev? i think while prev is correct way

            # 1,2,3,4,5,6   slow stops 4 fast is past 6
            # 1,2,3,4,5 slow =3 fast = 5
            #12321
            #1,2,3,3,2,1

            # slow wil always have 1 more value
            # odd case i get what about even i think slow has 2 more vals
        