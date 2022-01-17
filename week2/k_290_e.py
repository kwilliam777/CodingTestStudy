class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patD = {}
        sD = s.split(" ")
        if len(pattern) != len(sD):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in patD:
                if sD[i] in patD.values():
                    return False
                patD[pattern[i]] = sD[i]
            else:
                if patD[pattern[i]] != sD[i]:
                    return False
        return True