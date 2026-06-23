# working with a tree
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self,root: TreeNode):
        arrRes = []

        def dfs(node):
            if not node:
                arrRes.append("N")
                return

            # preorder
            arrRes.append(str(node.val)) # self
            dfs(node.left) # left
            dfs(node.right) # right

        dfs(root)
        result = (",").join(arrRes)
        return result

        # preorder order traversal
        # 1,2,null,null,3,4,null,null,5,null,null

        # recrusion dfs

    def deserialize(self, s: str):
        vals = s.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i])) # create node
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


    

