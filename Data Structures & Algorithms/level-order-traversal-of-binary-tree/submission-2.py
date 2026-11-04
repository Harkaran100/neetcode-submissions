# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            currLevel = []
            levelLen = len(queue)
            for i in range(levelLen):
                popVal = queue.popleft()
                if popVal:
                    currLevel.append(popVal.val)
                    queue.append(popVal.left)
                    queue.append(popVal.right)
            if currLevel:
                res.append(currLevel)
        return res

            
        