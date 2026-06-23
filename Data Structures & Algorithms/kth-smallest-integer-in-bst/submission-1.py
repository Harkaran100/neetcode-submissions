# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tracker = []
        counter = 0
        currentNode = root
        while currentNode or tracker:
            while currentNode:
                # to see what we must come back to
                tracker.append(currentNode)
                currentNode = currentNode.left
            # now all the way at left
            counter +=1
            # pop back up to none null
            currentNode = tracker.pop()

            if counter == k:
                return currentNode.val
            currentNode = currentNode.right
        