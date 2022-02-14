class Solution:
    def bitwiseComplement(self, n: int) -> int:
        test = bin(n)
        result = test[0:2]
        for i in range(2,len(test)):
            result += '0' if test[i] == '1' else '1'
        return int(result,2) 