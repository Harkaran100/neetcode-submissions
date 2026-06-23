# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # root value
        root = TreeNode(preorder[0])
        # seperates left and right subtree
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

        


        #notes
        # first of preorder is root
        # find this value in inorder and use it to seperate left and right subtrees
        # use dfs to continue this on each subtree

        #pre order is [1,2,3,4]
        # inorder is [2,1,3,4]
        #post order is [2,4,3,1]
        # output should be [1,2,3,null,null,null, 4]
