# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        if p == None and q == None: return True
        if (p == None and q != None) or (p != None and q == None): return False
        
        def check(p,q):
            if p.val!=q.val: return False
            
            pl = p.left if p.left != None else None
            pr = p.right if p.right != None else None
            ql = q.left if q.left != None else None
            qr = q.right if q.right != None else None
            
            # print(pl,pr,ql,qr)
            val1 = True
            val2 = True
            
            if (pl == None and ql != None) or (pl != None and ql == None):
                print("1")
                val1 = False
            elif pl!=None and ql!=None:
                print("2", pl,ql)
                val1 = check(pl,ql)
            
            if (pr == None and qr != None) or (pr != None and qr == None):
                print("3")
                val2 = False
            elif pr!=None and qr!=None:
                print("4")
                val2 = check(pr,qr)
            return val1 and val2
        
        return True if check(p,q) != False else False
    
    
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
        
#         if p and q and p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
#         return False
