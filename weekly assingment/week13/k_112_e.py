class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return
        targetSum -= root.val
        if targetSum == 0 and root.right == None and root.left == None: return True
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        
        
