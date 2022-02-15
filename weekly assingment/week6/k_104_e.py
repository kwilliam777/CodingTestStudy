# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        def deeper(root):
            if root.left == None and root.right == None: return 1
            l,r = 0,0
            if root.left != None: l += deeper(root.left)
            if root.right != None: r += deeper(root.right)
            return max(l,r)+1
        return deeper(root)