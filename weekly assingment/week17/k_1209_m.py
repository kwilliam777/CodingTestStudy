class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        for i in range(len(s)-k,-1,-1):
            if s[i:i+k].count(s[i])==k:
                s=s[:i]+s[i+k:]
        return s
