"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return copy.deepcopy(head)
    
#----------나의 망한 코드-----------
#         nodes = []
#         pointer = head
#         while pointer:
#             nextran = None if pointer.random == None else pointer.random.val
#             nodes.append([pointer.val,nextran])
#             pointer = pointer.next
            
#         result = Node(0)
#         pointer = result
#         save = [None]*(max([i[0] for i in nodes if i[0] != None])+1)
        
#         for i in nodes:
#             pointer.next = Node(i[0])
#             pointer = pointer.next
#             save[i[0]] = pointer            
        
#         pointer = result.next
#         for i in nodes:
#             if i[1] == None:
#                 pointer.random = None
#             else:
#                 pointer.random = save[i[1]]
#             pointer = pointer.next
            
#         return result.next
        
        
        
        
class Solution(object): 
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldToCopy ={None:None}

        cur = head
        while cur:
            copy =  Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]  
            cur=cur.next
        return oldToCopy[head] 
