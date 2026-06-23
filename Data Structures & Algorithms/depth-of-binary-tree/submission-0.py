# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # do dfs entire thing and return length of longest path
        # do first dfs path and count length each time
        # compare new path to max path and make longer one max path
        # once dfs done return max path 
        #unsure if this is recursion
        