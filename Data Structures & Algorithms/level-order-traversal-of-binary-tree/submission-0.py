# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            levelLen = len(queue)
            level = []
            for i in range(levelLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res

        
       # must use bfs as it makes sense
       # need to utilize a queue
       # variable to keep track of number of nodes at each level
       # use variable to get the x number of nodes from queue