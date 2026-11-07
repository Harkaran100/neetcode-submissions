class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # visit set
        visited = set()
        adjList = {}

        # prev to prevent false cycles
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for i in adjList[node]:
                if i == prev:
                    continue
                if not dfs(i,node):
                    return False
            return True

        # adjList (empty)
        for i in range(n):
            adjList[i] = []
    
        # populate adjList
        for edge in edges:
            node1, node2 = edge
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        print(adjList)

        return (dfs(0,-1)) and (n == len(visited))