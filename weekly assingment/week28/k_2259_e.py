class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        number+="a"
        for i in range(len(number)):
            if number[i]==digit:
                res.append(number[:i]+number[i+1:])
        return max(res)[:-1]
