class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connected= [points.pop()]
        cost = 0
        while points:
            low = 10000000
            rec = []
            for i in connected:
                for j in points:
                    manh = abs(i[0]-j[0])+abs(i[1]-j[1])
                    if manh < low:
                        low = manh
                        rec = j
            connected.append(rec)
            points.remove(rec)
            cost+=low
            # print(connected, points, cost)
        return cost
    
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
#         while d:
#             x, y = min(d, key=d.get)  # obtain the current minimum edge
#             res += d.pop((x, y))      # and remove the corresponding point
#             for x1, y1 in d:          # for the rest of the points, update the minimum manhattan distance
#                 d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
#         return res
