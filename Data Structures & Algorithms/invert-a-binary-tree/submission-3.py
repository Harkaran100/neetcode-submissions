# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self,root: [int]):
        if not root:
            return None
        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursion to do it all the way down the tree (dfs)
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
