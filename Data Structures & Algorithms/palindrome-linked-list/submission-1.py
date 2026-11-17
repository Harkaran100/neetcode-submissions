# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindromeCheck = []
        while head:
            palindromeCheck.append(head.val)
            head = head.next
        print(palindromeCheck)
        left = 0
        right = len(palindromeCheck) -1
        while right >= left:
            if palindromeCheck[left] == palindromeCheck[right]:
                left += 1
                right -= 1
            else: 
                return False
        return True

            #1221   12321 head=[2,1]
        