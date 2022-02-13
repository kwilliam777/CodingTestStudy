class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        count=[-1 for i in range(len(cost)+1)]

        
        def climb_cost (cost,location) -> int:
            if location <= 1 :
                count[location] = 0
                return 0
            
            elif count[location] == -1 :
                a=climb_cost(cost,location-1)+cost[location-1]
                b=climb_cost(cost,location-2)+cost[location-2]
                count[location]=min(a,b)
                return count[location]
            else :
                return count[location]
        
        location = len(cost)        
        return climb_cost(cost,location)
        
    
        