# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        # root.val is top
        # sorted tree 
        # if p and q lie on diffrent sides of tree then root.val will be lca
        # if p or q empty return null
        # if both p and q on same side from root, call recursive function on that side
        #what to do if q is decendant of p how to make output return p??
    def lowestCommonAncestor(self, root: [], p, q):
        if not p or not q:
            return None
        if ((root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val)):
            return root
        if ((root.val > p.val) and (root.val > q.val)):
            return self.lowestCommonAncestor(root.left, p ,q)
        if (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p ,q)
        if (root.val == p.val):
            return root
        if (root.val == q.val):
            return root