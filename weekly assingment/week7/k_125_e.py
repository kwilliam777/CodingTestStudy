class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = [i.lower() for i in s if i.isalnum()]
        return st == st[::-1]
