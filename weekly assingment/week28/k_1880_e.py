class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = int(''.join([str(ord(i)-97) for i in firstWord]))
        s = int(''.join([str(ord(i)-97) for i in secondWord]))
        t = int(''.join([str(ord(i)-97) for i in targetWord]))
        return f+s==t
