class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low<= node.val <= high:
                    self.ans += node.val
                    #print(node.val)
                if node.val>low:
                    dfs(node.left)
                if node.val<high:
                    dfs(node.right)
        self.ans = 0
        dfs(root)