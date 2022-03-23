class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2: target += 1
            else: target //= 2

        return ans + startValue - target
    
    
#하나도 못품...
#attempt 2    
#         count = 0 if target%2==0 else 1
#         poss = [target] if count == 0 else [target+1]
        
#         while poss[-1] != 1:
#             poss.append(poss[-1]//2)
        
#         while startValue != poss[-1]:
            
#attempt 1
#         count = 0
#         while startValue <= target:
#             startValue *= 2
#             count += 1
        
#         while startValue != target:
#             startValue -= 1
#             count += 1
        
#         return count
