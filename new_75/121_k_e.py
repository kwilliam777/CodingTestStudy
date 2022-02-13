class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestP, maxben = float("inf"), 0
        for price in prices:
            benefit = price - lowestP
            maxben = max(maxben, benefit)
            lowestP = min(lowestP, price)
        return maxben

        
#         maxben = 0
#         lowind = -1
#         highind = -1
#         for i in range(len(prices)):
#             if lowind != -1 and prices[i] >= prices[lowind]:
#                 pass
#             else:
#                 for j in range(i+1,len(prices)):
#                     if highind != -1 and prices[j] <= prices[highind]:
#                         pass
#                     else:
#                         temp = prices[j] - prices[i]
#                         if maxben < temp:
#                             maxben = temp
#                             highind = j
#                             lowind = i
#                             print(prices[i],prices[j])
                
#         return maxben


