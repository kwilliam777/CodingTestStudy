# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         q = [(0, root)]
#         ans = 0
#         while q:
#             temp = []
#             for i in range(len(q)):
#                 ind, node = q.pop(0)
#                 temp.append(ind)
#                 if node.left:
#                     q.append((2*ind+1, node.left))
#                 if node.right:
#                     q.append((2*ind+2, node.right))
#             ans = max(ans, max(temp)-min(temp)+1)
#         return ans
    
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # Treat tree as Heap array and save idx as 2*i and 2*i + 1
#         # diff of first and last node when level ends is the result
#         if not root: return 0
#         q = [[root,1]]
#         maxWidth = 0
#         while q:
#             maxWidth = max(maxWidth,q[-1][1] - q[0][1] + 1) # find the difference for upcomming queue
#             for _ in range(len(q)):
#                 curr,idx = q.pop(0)
#                 if curr.left: q.append((curr.left,idx*2))
#                 if curr.right: q.append((curr.right, idx*2+1))
#         return maxWidth
# 		# like if you find it useful
