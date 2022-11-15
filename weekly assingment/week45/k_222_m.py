class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        nodes = [root]
        count = 0
        while nodes:
            temp = nodes.pop()
            count+=1
            if temp.left: nodes.append(temp.left)
            if temp.right: nodes.append(temp.right)
        return count
