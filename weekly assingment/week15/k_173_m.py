class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.pointer = -1
        def trace(root):
            if not root: return
            if root.left: trace(root.left)
            self.nodes.append(root)
            if root.right: trace(root.right)
        trace(root)

    def next(self) -> int:
        self.pointer+=1
        return self.nodes[self.pointer].val

    def hasNext(self) -> bool:
        return True if len(self.nodes) > self.pointer+1 else False

    
    
# class BSTIterator:
#     # @param root, a binary search tree's root node
#     def __init__(self, root):
#         self.stack = list()
#         self.pushAll(root)

#     # @return a boolean, whether we have a next smallest number
#     def hasNext(self):
#         return self.stack

#     # @return an integer, the next smallest number
#     def next(self):
#         tmpNode = self.stack.pop()
#         self.pushAll(tmpNode.right)
#         return tmpNode.val
        
#     def pushAll(self, node):
#         while node is not None:
#             self.stack.append(node)
#             node = node.left
