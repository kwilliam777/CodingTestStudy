"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#gkskeh ahtvna sork vnsrj dksla
# class Solution:

    # recursive
#     def connect(self, root):
#         if root and root.left and root.right:
#             root.left.next = root.right
#             if root.next:
#                 root.right.next = root.next.left
#             self.connect(root.left)
#             self.connect(root.right)
 
#     # BFS       
    # def connect(self, root):
    #     if not root:
    #         return 
    #     queue = [root]
    #     while queue:
    #         curr = queue.pop(0)
    #         if curr.left and curr.right:
    #             curr.left.next = curr.right
    #             if curr.next:
    #                 curr.right.next = curr.next.left
    #             queue.append(curr.left)
    #             queue.append(curr.right)

#     # DFS 
    # def connect(self, root):
    #     if not root:
    #         return 
    #     stack = [root]
    #     while stack:
    #         curr = stack.pop()
    #         if curr.left and curr.right:
    #             curr.left.next = curr.right
    #             if curr.next:
    #                 curr.right.next = curr.next.left
    #             stack.append(curr.right)
    #             stack.append(curr.left)


        return root
