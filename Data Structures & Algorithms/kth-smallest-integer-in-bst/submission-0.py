# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tracker = [] # to track nodes inorder traversal
        counter = 0 # so we know when we reach k element and can return
        currentNode = root # useful to know which node currently on

        while currentNode or tracker:
            while currentNode:
                tracker.append(currentNode)
                currentNode = currentNode.left

            currentNode = tracker.pop()
            counter += 1

            if counter == k:
                return currentNode.val
            
            currentNode = currentNode.right

        # since bst we can do inorder traversal and return kth smallest element
        # first try to go left once cannot then visit/ add in stack once done
        # go right, if cannot go up one level
        #what should be basecase? root.val = null?