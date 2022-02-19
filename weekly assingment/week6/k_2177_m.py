class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0: return [-1,0,1]
        elif num == 3: return [0,1,2]
        elif num < 6 or num%3 != 0: return []
        base = num//3
        return [base-1,base,base+1]
