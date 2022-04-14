# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        que = [root]
        while que:
            temp = que.pop()
            if temp.val == val: return temp
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
    
    
# class Solution(object):
#     def searchBST(self, root, val):
#         trav = root
#         while trav:
#             if trav.val == val: return trav
#             elif trav.val < val: trav = trav.right
#             else: trav = trav.left
