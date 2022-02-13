class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        result = [int(i) for i in list(str(num))]
        addA = 0
        while len(result) != 1:
            addA = sum(result)
            result = [int(i) for i in list(str(addA))]
            
        return addA
        # return 1 + (num - 1) % 9 if num else 0  