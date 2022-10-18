from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'
        for i in range(n-1):
            output = ''.join([str(len(list(g))) + k for k, g in groupby(output)])
        return output
