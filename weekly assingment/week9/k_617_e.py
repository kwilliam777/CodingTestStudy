# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None and root2==None: return None
        elif root1==None: return root2
        elif root2==None: return root1
        
        ans = TreeNode(root1.val+root2.val)
        
        def mt(ans,r1,r2):
            if r1 == None and r2 == None:
                return
            rightchange = False
            leftchange = False
            right = 0
            left = 0
            if r1!=None:
                if r1.right!=None:
                    right+=r1.right.val
                    rightchange = True
                if r1.left!=None:
                    left+=r1.left.val
                    leftchange = True
            if r2!=None:
                if r2.right!=None:
                    right+=r2.right.val
                    rightchange = True
                if r2.left!=None:
                    left+=r2.left.val
                    leftchange = True
                    
            if rightchange:
                ans.right = TreeNode(right)
            if leftchange:
                ans.left = TreeNode(left)
            
            mt(ans.right,r1.right if r1!=None else None,r2.right if r2!=None else None)
            mt(ans.left,r1.left if r1!=None else None,r2.left if r2!=None else None)
        

        mt(ans,root1,root2)
        return ans
        
        
        
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1:
#             return t2
#         elif not t2:
#             return t1
#         else:
#             res = TreeNode(t1.val + t2.val)
#             res.left = self.mergeTrees(t1.left, t2.left)
#             res.right = self.mergeTrees(t1.right, t2.right)
#         return res
