class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, side = "left") -> TreeNode:
        if d == 1:
            res = TreeNode(v)
            setattr(res, side, root)
            return res
        if root:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1, 'right')
        return root
