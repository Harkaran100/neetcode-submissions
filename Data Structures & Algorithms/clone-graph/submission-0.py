"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        origToCopy = {}

        def dfs(currNode):
            if currNode in origToCopy:
                return origToCopy[currNode] # return the copy

            # make copy
            newNode = Node(currNode.val)
            # store in hashmap
            origToCopy[currNode] = newNode

            # explore neighbors 
            for neighbor in currNode.neighbors:
                clonedNeighbor = dfs(neighbor)
                newNode.neighbors.append(clonedNeighbor)
            return newNode

        return dfs(node)


        