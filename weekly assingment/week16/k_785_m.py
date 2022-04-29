class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        left = [0]
        right = []
        rec = [(i,v) for i,v in enumerate(graph)]
        visited = []
        while rec:
            ind,temp = rec.pop(0)
            if len(temp)==0: left.append(ind)
            elif ind in left:
                right+=temp
                for i in temp:
                    left += graph[i]
            elif ind in right:
                left+=temp
                for i in temp: right += graph[i]
            else:
                for i in temp:
                    if i in left: right.append(ind)
                    elif i in right: left.append(ind)
                    else:
                        if ind in visited:
                            left.append(ind)
                            right+=temp
                        else:
                            visited.append(ind)
                            rec.append([ind,temp])
            
            ind+=1

        return False if len(set(left))+len(set(right))!=len(graph) else True
       

#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         visited = set()
#         two_color = [set(), set()]
#         for i in range(len(graph)):
#             if i not in visited:
                
#                 queue = [(i, 0)]
#                 while queue:
#                     node, level = queue.pop()
#                     visited.add(node)
#                     two_color[level].add(node)
                
#                     for neighbor in graph[node]:
#                         if neighbor in two_color[level]:
#                             return False
#                         if neighbor not in visited:
#                             queue.append((neighbor, 1 if level == 0 else 0))
                    
#         return True
