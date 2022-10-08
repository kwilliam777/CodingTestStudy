class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(root, val):
            if root:
                if root.left==None and root.right==None:
                    if val+root.val==targetSum:return True
                    else:return False
                else:
                    return check(root.left,val+root.val) or check(root.right,val+root.val)
        return check(root,0)
 
