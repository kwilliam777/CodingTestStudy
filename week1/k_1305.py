# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        def getAll(root):
            result.append(root.val)
            if root.left != None: getAll(root.left)
            if root.right != None: getAll(root.right)
        if root1 != None: getAll(root1)
        if root2 != None: getAll(root2)
        return sorted(result)