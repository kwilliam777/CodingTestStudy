class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest,found = 0, False
        for i in range(len(s)):
            if longest < len(s[i:]):
                if s[i+longest] in s[i:i+longest]: continue
                else:
                    for j in range(i+1,len(s)):
                        if s[j] in s[i:j]:
                            if longest < len(s[i:j]):  
                                longest = len(s[i:j])
                                found = True
                            break
                        elif s[i:j+1] == s[i:] and longest < len(s[i:]):
                            longest = len(s[i:])
                            found = True
        return longest if found else len(s) 
