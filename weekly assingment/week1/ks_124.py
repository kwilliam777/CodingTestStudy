# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        maxSum = 0
        leftMax = 0
        rightMax = 0
        
        def findCenter(root):
            vals = root.val
            leftVal = 0
            rightVal = 0

            if root.left != None:
                leftVal = valsUnder(root.left)

            if root.right != None:
                rightVal = valsUnder(root.right)
                
            if leftVal <= 0 and rightVal <= 0:
                pass
            elif leftVal <= 0 and rightVal > 0:
                vals += rightVal
            elif rightVal <= 0 and leftVal > 0:
                vals += leftVal
            else:
                vals += rightVal + leftVal
            
            maxSum = vals
            leftMax = -inf
            rightMax = -inf
            
            if root.left != None:
                leftMax = findCenter(root.left)

            if root.right != None:
                rightMax = findCenter(root.right)
                
            if maxSum < leftMax:
                return leftMax
            elif maxSum < rightMax:
                return rightMax
            else:
                return maxSum
                
        def valsUnder(root):
            result = root.val
            leftVal = 0
            rightVal = 0
            
            if root.left != None:
                leftVal = valsUnder(root.left)
            if root.right != None:
                rightVal = valsUnder(root.right)
            
            if leftVal < rightVal:
                return result + rightVal
            else:
                return result + leftVal
        
        
        return findCenter(root)

