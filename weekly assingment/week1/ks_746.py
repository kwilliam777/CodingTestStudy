class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = 0
        test = [-1 for i in range(len(cost))]
        def find(cost,index):
            if index == 0:
                return cost[0]
            elif index == 1:
                return cost[1]
            else:
                if test[index-1] == -1:
                    test[index-1] = find(cost,index-1)

                if test[index-2] == -1:
                    test[index-2] = find(cost,index-2)

                return min(test[index-1],test[index-2])+cost[index]
                
        return min(find(cost, len(cost)-1), find(cost,len(cost)-2))
      
