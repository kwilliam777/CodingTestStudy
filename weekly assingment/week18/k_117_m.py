# from copy import deepcopy
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root==None: return
#         nodes = [root,None]
#         rec = [root]
        
#         while nodes[-2]!=None:
#             child = []
#             while rec:
#                 temp = rec.pop(0)
#                 if temp==None: break
#                 if temp.left!=None: child.append(temp.left)
#                 if temp.right!=None: child.append(temp.right)
#             rec = copy.deepcopy(child)
#             nodes+=child
#             nodes.append(None)
            
#         print([i.val if i!=None else "None" for i in nodes])
        
#         for i in range(len(nodes)-1):
#             if nodes[i]!=None:
#                 nodes[i].next=nodes[i+1]
#                 print(nodes[i].next.val if nodes[i].next != None else None)

                
        # return root
class Solution:    
    def connect(self, root: 'Node') -> 'Node':
        tmp = dummy = Node(-1, None, None, None)
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None
            
        return res
