class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x != abs(x):
        #     return False
        # if x < 10:
        #     return True
        # li = list(str(x))
        # lir = copy.deepcopy(li)
        # lir.reverse()
        # if li == lir:
        #     return True
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False