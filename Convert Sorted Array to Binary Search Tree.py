class Solution(object):
    def sortedArrayToBST(self, nums):
        def bst(l,r) :
            if l > r : return None
            mid = (l+r)//2
            return TreeNode(nums[mid], bst(l,mid-1), bst(mid+1,r)) 
            
        return bst(0,len(nums)-1)