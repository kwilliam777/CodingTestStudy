from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(Counter(str(bin(i)[2:]))['1'])
        return ans
        # return [b_val.count("1") for b_val in [bin(i)[2:] for i in range(n + 1)]]
