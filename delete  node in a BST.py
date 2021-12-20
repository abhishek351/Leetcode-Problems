class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if root.val == key:
            if not root.right: return root.left
            
            if not root.left: return root.right
            
            # find max in the left subtree
            left_max = root.left
            while left_max.right:
                left_max = left_max.right
            
            # connect the root.right to the root.left and return the root.left
            left_max.right = root.right
            return root.left


        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root