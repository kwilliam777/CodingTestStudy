class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        
        while len(stones) > 1:
            stones.sort(reverse = True)
            first = stones.pop(0)
            second = stones.pop(0)
            if first != second:
                stones.append(first-second)
                
        return 0 if len(stones) < 1 else stones[0]
            
