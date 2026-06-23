# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #since it is a tree problem I am thinking recursion
        # can be bfs or dfs

        #base case
        if not root:
            return None
        
        # switch left and right children 
        temporary = root.left
        root.left = root.right
        root.right = temporary

        # recursive step
        self.invertTree(root.left) 
        self.invertTree(root.right)

        return root


        