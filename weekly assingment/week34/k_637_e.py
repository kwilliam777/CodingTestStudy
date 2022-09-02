# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        child = [[root]]
        
        while child:
            nodes = child.pop()
            length = len(nodes)
            rec = []
            val = 0
            for node in nodes:
                if node.left!=None:rec.append(node.left)
                if node.right!=None:rec.append(node.right)
                val += node.val
            if len(rec)>0: child.append(rec)
            res.append(val/length)
        return res
