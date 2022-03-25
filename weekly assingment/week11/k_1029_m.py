class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        costs = sorted(costs,key = lambda x:abs(x[0]-x[1]),reverse = True)
        acount = 0
        bcount = 0
        ans = 0
        
        for i in costs:
            if bcount == n or (i[0]<i[1] and acount < n):
                ans+=i[0]
                acount+=1
            else:       
                ans+=i[1]
                bcount+=1
                
        return ans 
