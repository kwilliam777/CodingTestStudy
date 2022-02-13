class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        check = [0]*60
        result = 0
        for t in time:
            rem = t % 60
            target = (60 - rem) % 60
            result += check[target]
            check[rem] += 1
        return result