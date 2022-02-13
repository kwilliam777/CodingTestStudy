class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=sys.maxsize

        for value in prices:
            if min_price > value :
                min_price=value
            elif profit < value-min_price :
                profit=value-min_price
        return profit
                
