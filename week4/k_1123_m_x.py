# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         d = 0
#         dlist = {0:[root]}
        
#         while len(dlist[d]) != 0:
#             dlist[d+1] = []
#             for node in dlist[d]:
#                 if node.left != None: dlist[d+1].append(node.left)
#                 if node.right != None: dlist[d+1].append(node.right)
#             d += 1
        
#         if len(dlist[d]) == 0: d -= 1
#         if len(dlist[d]) == 1: return dlist[d][0]
#         elif len(dlist[d]) == 2:
#             for node in dlist[d-1]:
#                 if node.left == dlist[d][0] and node.right == dlist[d][1]:
#                     return node
#             return root
#         else: 
#             return root
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root,level):
            nonlocal deepest 
            nonlocal ans
            if not root: return level-1
            l = dfs(root.left,level+1)
            r = dfs(root.right,level+1)
            deepest = max(deepest,level)
            if l == deepest and r == deepest: ans=root
            return max(l,r)
        deepest = ans = 0
        dfs(root,0)
        return ans