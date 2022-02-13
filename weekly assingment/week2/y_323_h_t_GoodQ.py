from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        edge = defaultdict(list)        
        
        count = 0
        for _from, _to in tickets:
            edge[_from].append(_to)
            count+=1
        
        for i in edge :
            _new=[]
            _new=list(edge[i])
            _new.sort()
            edge[i]=_new
        
        start="JFK"
        itinerary=[]
        
        def DFS (start, edge, itinerary) :
            itinerary.append(start)
            
            if (len(itinerary)==count+1) :
                return itinerary
            
            #if not edge[start] or len(edge[start]) < 1 :
            #    return False
            
            dsts= list(edge[start])
            for _next in dsts:
                edge[start].remove(_next)
                result = DFS (_next,edge,itinerary)                
                if result : return result
                itinerary.pop()
                edge[start].append(_next)

        return DFS(start, edge,itinerary)

                