class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        vals = []
        nodes = []
        pointer = root
        def collect(pointer):
            if pointer == None: return 
            if pointer.left:
                collect(pointer.left)
            vals.append(pointer.val)
            nodes.append(pointer)
            if pointer.right:
                collect(pointer.right)
        
        collect(pointer)
        temp = sorted(vals)
        swap = [i for i in range(len(temp)) if temp[i]!=vals[i]]
        
        swap1 = nodes[swap[0]]
        swap2 = nodes[swap[1]]
        
        swap1.left,swap1.right = swap2.left,swap2.left
                
        print(root)
        
# XXXXXXXXXXXXXXXXXXX
# class Solution(object):
#     def recoverTree(self, root):
#         self.first, self.second, self.prevNode = None, None, None # Create three nodes.
#         self.inOrder(root) # Calling the function
#         self.first.val, self.second.val = self.second.val, self.first.val 
        
#     def inOrder(self, root):
#         if not root:
#             return
#         self.inOrder(root.left)
        
#         if self.prevNode: # To handle the case of first node, because we make it prev to begin with
#             if self.prevNode.val > root.val: # Check property violation
#                 if not self.first: 
#                     self.first = self.prevNode # Found first pair
#                 self.second = root # If the second pair is found then simply assign the smaller element of the   pair as the second guy, it works for single pair easily, as it wont get             updated again in that case.
                
#         self.prevNode = root
#         self.inOrder(root.right)
