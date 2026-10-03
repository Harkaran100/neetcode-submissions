# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: # edge case
            return True
        return self.valid(root,float("-inf"), float("inf"))
    def valid(self,node,lowerB,upperB):
        if not node:
            return True
        if not lowerB < node.val < upperB:
            return False
        left = self.valid(node.left,lowerB,node.val)
        right = self.valid(node.right,node.val,upperB)

        return (left and right)

        #               6
        #          4         10
        #       2     5    8     12
        #
        #
        #

        
        