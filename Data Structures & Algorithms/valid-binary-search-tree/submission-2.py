# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,lower_bound,upper_bound): # helper func
            if not node:
                return True
            if not lower_bound < node.val < upper_bound:
                return False
            left = valid(node.left,lower_bound,node.val) # update right boundary
            right = valid(node.right,node.val,upper_bound) # update left boundary

            return (left and right)

        if not root:
            return True
        return(valid(root,float('-inf'), float('inf')))

    