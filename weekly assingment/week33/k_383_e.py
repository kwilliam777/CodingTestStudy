from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return True if len(Counter(ransomNote)-Counter(magazine)) == 0 else False
