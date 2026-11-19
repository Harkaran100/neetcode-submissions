# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs pass in p and q
        # base case not root
        def dfs(p,q):
            # base cases
            if not p and not q: # both not there
                return True
            elif not p or not q: # one is missing
                return False
            elif p.val != q.val: # different values
                return False
            else:
                left = dfs(p.left,q.left)
                right = dfs(p.right,q.right)

                return left and right



        return(dfs(p,q))