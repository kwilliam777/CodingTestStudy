# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return []
        pointer = [[root]]
        res = []
        while pointer:
            par = pointer.pop()
            if len(par)==0: break
            res.append(par[-1].val)
            child = []
            for i in par:
                if i.left!=None:
                    child.append(i.left)
                if i.right!=None:
                    child.append(i.right)
            pointer.append(child)
        return res
            

    # def rightSideView(self, root):
    #     if not root:
    #         return []
    #     right = self.rightSideView(root.right)
    #     left = self.rightSideView(root.left)
    #     return [root.val] + right + left[len(right):]
