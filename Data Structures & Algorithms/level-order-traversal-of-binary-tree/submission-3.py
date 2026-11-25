# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       # traverse in bfs, make sense since tree level
       # bfs is done with a queue
       # somehow maintain a len of current level
       # make copy from deque of that len and put in res

       # for the len we can do a for loop of that len where we pop that many elements and once done we are at enxt level

       #  of n time and o of n total space made up o of l + nodes per level where l is levels

        result = []
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result.append([root.val])
        while queue:
            levelLen = len(queue)
            level = []
            for i in range(levelLen):
                popped = queue.popleft()

                if popped.left:
                    leftVal = popped.left
                    queue.append(leftVal)
                    level.append(leftVal.val)

                if popped.right:
                    rightVal = popped.right
                    queue.append(rightVal)
                    level.append(rightVal.val)

            if len(level) > 0:
                result.append(level)
        return result



