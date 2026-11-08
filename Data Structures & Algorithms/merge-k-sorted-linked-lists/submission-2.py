# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # 2 at a time, while len(list) > 1 if 1 output it
        while len(lists) > 1:
            mergedList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                dummy = ListNode()
                curr = dummy
                while l1 and l2:
                    if l1.val > l2.val:
                        curr.next = l2
                        l2 = l2.next
                    else:
                        curr.next = l1
                        l1 = l1.next
                    curr = curr.next
                # 1 list may be remaining
                if l1:
                    curr.next = l1
                if l2:
                    curr.next = l2
                mergedList.append(dummy.next)
            lists = mergedList
        return lists[0]
                



                


# another thing that comes to mind to do it in less time is merge 2 lists at a time so somwthing. like while lists > 1 return when 1, and account for edge case theres no lists
# this will allow for much less repeated work
# time will be o of n space wise im thinking same thign have an extra link list to append to while trav then replace