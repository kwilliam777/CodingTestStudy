# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result1 = []
        result2 = []
        def getleave(root, arr):
            if root.right == None and root.left == None:
                arr.append(root.val)
            if root.left != None:
                getleave(root.left, arr)
            if root.right != None:
                getleave(root.right, arr)
        getleave(root1,result1)
        getleave(root2,result2)
                
        if len(result1) != len(result2):
            return False
        
        for i in range(len(result1)):
            if result1[i] != result2[i]:
                return False
            
        return True

                