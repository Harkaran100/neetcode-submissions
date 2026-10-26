# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val,None,None)

        current = root

        while current:
            if val > current.val and current.right: # move to right sub tree
                current = current.right
            elif val < current.val and current.left:
                current = current.left
            else: # child node does not exist
                insertNode = TreeNode(val,None,None)
                if val < current.val: # how to create Node
                    current.left = insertNode
                    break
                else:
                    current.right = insertNode
                    break
        return root
                
