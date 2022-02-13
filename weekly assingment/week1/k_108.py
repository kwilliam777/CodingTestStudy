# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        elif len(nums) == 1: return TreeNode(nums[0])
        else:
            mid = int(len(nums)/2)
            root = nums[mid]
            return TreeNode(root, 
                            self.sortedArrayToBST(nums[0:mid]),                
                            self.sortedArrayToBST(nums[mid+1:]))