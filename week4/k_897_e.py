# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def gettree(root, result) -> list[TreeNode]:
            temp = TreeNode(root.val)
            if root.left == None and root.right == None:
                result.append(temp)
                return result
            if root.left != None:
                result = gettree(root.left,result)
                result.append(temp)
            if root.right != None:
                if temp not in result:
                    result.append(temp)
                result = gettree(root.right,result)
            return result
        
        nodes = []
        
        tree = gettree(root,nodes)
        result = 0
        for i in range(len(tree)):
            if i == 0:
                result = tree[i]
            else:
                tree[i-1].right = tree[i]
        return result 
#     def increasingBST(self, root):
#         def inorder(node):
#             if node:
#                 yield from inorder(node.left)
#                 yield node.val
#                 yield from inorder(node.right)

#         ans = cur = TreeNode(None)
#         for v in inorder(root):
#             cur.right = TreeNode(v)
#             cur = cur.right
#         return ans.right      