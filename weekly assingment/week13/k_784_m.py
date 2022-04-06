class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i in range(len(s)):
            temp = ans
            for j in range(len(ans)):
                temp = ans.pop(0)
                if s[i].isalpha():
                    ans.append(temp+s[i].lower())
                    ans.append(temp+s[i].upper())
                else:
                    ans.append(temp+s[i])
        return ans 
