class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numint = ""
        ans = []
        for i in num: numint+=str(i)
        temp = k+int(numint)
        for i in str(temp): ans.append(i)
        return ans
            
        
        # return [int(i) for i in str(int(''.join([str(i) for i in num]))+k)]
