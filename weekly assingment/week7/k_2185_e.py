class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([i for i in words if i[:len(pref)] == pref])
