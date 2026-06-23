# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap nodes
        temporary = root.left
        root.left = root.right
        root.right = temporary
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        #thinking pf recursion, possibly continue until the 
        #subtree no longer has another childnode
        # Once reached left and right values switch and exit
        #keep doing that till reach the top
        