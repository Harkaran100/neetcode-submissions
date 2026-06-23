# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # should turn into a str
        resArr = []
        # given in preorder
        # self,left,right
        
        def dfs(root):
            # base case:
            if root == None:
                resArr.append("Null") 
                return

            resArr.append(str(root.val)) # self

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        result = ",".join(resArr)
        return result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",") # ["1","2","3"]
        i = 0
        def dfs():
            nonlocal i
            # basecase
            if values[i] == "Null":
                i += 1
                return
            node = TreeNode(int(values[i])) # create node
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()


