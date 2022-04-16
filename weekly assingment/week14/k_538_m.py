# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        que = [root]
        vals = []
        while que:
            temp = que.pop()
            vals.append(temp.val)
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
            
        # print(sorted(vals))
        que = [root]
        while que:
            temp = que.pop()
            greater = sum([i for i in vals if i > temp.val])
            temp.val += greater
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
            
        return root
    
    
    
    
    
# class Solution:
# 	def convertBST(self, root: TreeNode) -> TreeNode:
# 		sum = 0
		
# 		def sol(root: TreeNode) -> TreeNode:
# 			nonlocal sum
# 			if root:
# 				sol(root.right)
# 				root.val += sum
# 				sum = root.val
# 				sol(root.left)
# 			return root
		
# 		return sol(root)
