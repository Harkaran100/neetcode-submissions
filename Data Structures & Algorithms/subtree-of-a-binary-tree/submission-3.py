# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if (self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)):
                return True

        # recurse this function
        return (self.isSubtree(root.left,subRoot) or
        self.isSubtree(root.right,subRoot))

    
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return (self.isSameTree(root.left,subRoot.left) and
            self.isSameTree(root.right,subRoot.right))
        
        
        # check is subroot exist in root
        # if not root return False
        # use a helper function for issameTree
        # only call helper if root.val and subRoot.val are same
        # recurse isubtree with root.left,subroot and root.right, subroot
        # because we are look for case where issametree will pickup when vals same
        # 
        