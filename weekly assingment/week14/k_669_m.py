class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root == None: return None
        
        while root and not (low <= root.val <= high):
            if root.val > low:
                root = root.left
            elif root.val < high:
                root = root.right
                
        lp = root
        rp = root
        lc = None if root == None else root.left
        rc = None if root == None else root.right
        
        while lc:
            if lc.val > low:
                lp.left = lc.right
            else:
                lp = lc
                lc = lc.left
            
        while rc:
            if rc.val < high:
                rp.right = rc.left
            else:
                rp = rc
                rc = rc.right
            
        return root
    
# class Solution:
# 	def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
# 		if not root: return root
# 		if root.val < low: return self.trimBST(root.right, low, high)
# 		if root.val > high: return self.trimBST(root.left, low, high)
# 		root.left = self.trimBST(root.left, low, high)
# 		root.right = self.trimBST(root.right, low, high)
# 		return root
