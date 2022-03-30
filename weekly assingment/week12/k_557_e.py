class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = []
        for word in s:
            temp = ""
            for l in range(len(word)-1,-1,-1):
                temp+=word[l]
            ans.append(temp)
        return (" ").join(ans)
    
    
        # return ' '.join(x[::-1] for x in s.split())
