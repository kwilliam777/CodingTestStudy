class Solution:
    def guessNumber(self, n: int) -> int:
        minn, maxx = 0, n
        val = (minn+maxx)//2
        res = guess(val)
        while res != 0:
            if res == -1:
                maxx = val
                val -= (maxx-minn+1)//2
            elif res == 1:
                minn = val
                val += (maxx-minn+1)//2
            res = guess(val)
        return val
