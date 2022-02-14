# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = []
        def findLeaf(location) :
            if location.right == None and location.left == None :
                result.append(location.val)
            if location.left != None :
                findLeaf(location.left)
            if location.right != None :
                findLeaf(location.right)
        
        findLeaf(root)
                    
        print(result)