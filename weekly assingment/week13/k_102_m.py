# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def deep(root,level):
            if root == None: return
            if len(ans)-1 < level: ans.append([root.val])
            else: ans[level].append(root.val)
            deep(root.left,level+1)
            deep(root.right,level+1)

        deep(root,0)
        return ans
