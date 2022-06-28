class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if num == int(num**(1/2))*int(num**(1/2)) else False
