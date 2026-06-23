# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        # case to continue checking main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self,mainTree,subTree):
        if not mainTree and not subTree:
            return True
        if mainTree and subTree and mainTree.val == subTree.val:
            return self.sameTree(mainTree.left,subTree.left) and self.sameTree(mainTree.right,subTree.right)
        return False