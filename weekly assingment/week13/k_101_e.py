# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None: return True
        elif root.left == None or root.right == None: return False
        r,l=[],[]
        self.ri,self.li = 0,0
    
        def symleft(root):
            if root == None: l.append("N")
            elif root.right == None and root.left == None: l.append(root.val)
            else:
                symleft(root.left)
                l.append(root.val)
                symleft(root.right)
            l.append(self.li)
            self.li+=1
            
        def symright(root):
            if root == None: r.append("N")
            elif root.right == None and root.left == None: r.append(root.val)
            else:
                symright(root.right)
                r.append(root.val)
                symright(root.left)
            r.append(self.ri)
            self.ri+=1

        symleft(root.left)
        symright(root.right)
        return r==l
    
    
    
#     def isSymmetric(self, root):
#         def isSym(L,R):
#             if L and R and L.val == R.val: 
#                 return isSym(L.left, R.right) and isSym(L.right, R.left)
#             return L == R
#         return not root or isSym(root.left, root.right)
    
    
