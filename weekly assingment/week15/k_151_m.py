class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ").join(reversed([i for i in s.split(" ") if len(i) > 0]))
