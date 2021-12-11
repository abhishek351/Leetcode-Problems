

class Codec:

    def serialize(self, root):
        res=[]
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        data =  data.split(",")
        
        def makeTree(idx):
            node = TreeNode(int(data[idx])) if data[idx] != "N" else None
            if node:
                node.left, idx = makeTree(idx+1)
                node.right, idx = makeTree(idx+1)
            return node, idx
        
        return makeTree(0)[0]
        