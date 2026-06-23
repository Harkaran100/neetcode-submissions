# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case ends recursion stack
        if not preorder or not inorder:
            return None
        
        # create root
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # in in order signifies the root everything to left is left everything to right is right

        root.left = self.buildTree(preorder[1:mid + 1],inorder[:mid])
        root.right = self.buildTree(preorder[mid +1:], inorder[mid + 1:])

        return root
        # preorder is self, left ,right
        # inorder is left,self right
        # we know in order goes all the way deep into left subtree
        # we know preorder head is root
        # how to use these facts
        # we can traverse entire inorder until we get val = preorder head
        # this will signify the entire left subtree
        # values being unique helps with this 

        #           1
        #         4    6
        #        2 3  7  8
        #   preorder [1,4,2,3,6,7,8]
        #   inorder [2,4,3,1,7,6,8]
        # by the time we reach root of preorder in inorder
        # we have left subtree inorder [2,4,3,1]
        # check pattern again, head of this subtree is 4, iterate through in order to find it
        # use this pattern via recursion
        