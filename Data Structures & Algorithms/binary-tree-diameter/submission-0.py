# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0 # self so member function and can be used in dfs

        # goal is to return the diamater which is made up of the longest left and longest right path combination
        # keep track of largest value
        def dfs(root):
            if not root:
                return 0
            # recursion
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res