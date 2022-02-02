# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None
        elif root.right == None and root.left == None:
            return root.val
       
        vals = [root.val]
        def helper(root,vals):
            if root.left != None:
                vals.append(root.left.val)
                helper(root.left,vals)
            if root.right != None:
                vals.append(root.right.val)
                helper(root.right,vals)
               
        helper(root,vals)
        return sorted(vals)[k-1]