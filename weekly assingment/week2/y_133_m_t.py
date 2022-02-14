"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node :
            return node
        
        visit ={}
        
        qu =deque([node])
        
        visit[node] = Node(node.val,[])
        
        while qu :
            n=qu.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in visit :
                    visit[neighbor] = Node (neighbor.val,[])
                    qu.append(neighbor)
                    
                visit[n].neighbors.append(visit[neighbor])
                
        return visit[node]