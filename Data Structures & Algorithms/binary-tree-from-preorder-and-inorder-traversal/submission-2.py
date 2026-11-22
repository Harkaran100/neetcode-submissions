# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        right = len(inorder) -1
        preOrderIndex = 0 # global
        inorderMap = {} # val -> index
        for num in range(len(inorder)):
            inorderMap[inorder[num]] = num

        def dfs(left,right):
            nonlocal preOrderIndex
            if left > right:
                return
            # find preorder in inorder and make root
            val = preorder[preOrderIndex]
            preOrderIndex += 1
            root = TreeNode(val)
            root.left = dfs(left, inorderMap[val] - 1)
            root.right = dfs(inorderMap[val] + 1,right)

            return root

        return dfs(0,right)

        # preorder is root left right
        # inorder is left, root, right

        # find first val of preorder in inorder
        # everything to the left is in left subtree everything in the right is in right subtree
        # use recursion and continue

        # need to account for binary with size on which ever side