class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root:
            root.left = self.removeLeafNodes(root.left,target)
            root.right = self.removeLeafNodes(root.right,target)
            return None if not root.left and not root.right and root.val==target else root
