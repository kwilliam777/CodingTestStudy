class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         diff = [heights[i]-heights[i-1] for i in range(1,len(heights))]
#         brick = bricks
#         ladder = ladders
#         save = []
        
#         for i in range(len(diff)):
#             if diff[i] > 0:
#                 save.append(diff[i])
#                 brick-=save[0]
                
#                 if brick <= 0:
#                     save.sort(reverse = True)
#                     maxi = save[0]
                    
#                     if i+1 < len(diff) and diff[i+1] > maxi:
#                         if ladder == 0:
#                             return i
#                         else:
#                             brick+=maxi
#                             ladder-=1
#                     else:
#                         save.pop(0)
#                         brick+=maxi
#                         ladder -=1
#         return len(heights)-1
    
    
    
    def furthestBuilding(self, H: List[int], bricks: int, ladders: int) -> int:
        jumps_pq = []
        for i in range(len(H) - 1):
            jump_height = H[i + 1] - H[i]
            if jump_height <= 0: continue
            heappush(jumps_pq, jump_height)
            if len(jumps_pq) > ladders:
                bricks -= heappop(jumps_pq)
            if(bricks < 0) : return i
        return len(H) - 1
