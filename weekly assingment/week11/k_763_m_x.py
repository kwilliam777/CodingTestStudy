class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1: return [1]
        
        result = []
        ind = 0
        done = False
        
        while not done:
            if ind == len(s): break
            temp = s[ind+1:].rfind(s[ind])
            print(ind,s[ind],temp)
            if temp == -1:
                result.append(1)
                ind += 1
            else:
                temp += 2
                while ind+temp<len(s)-1 and s[ind+temp] in s[ind:ind+temp]:
                    temp += 1
                result.append(temp)
                ind += temp
        
        return result
    

# class Solution(object):
#     def partitionLabels(self, S):
#         last = {c: i for i, c in enumerate(S)}
#         print(last)
#         j = anchor = 0
#         ans = []
#         for i, c in enumerate(S):
#             j = max(j, last[c])
#             if i == j:
#                 ans.append(i - anchor + 1)
#                 anchor = i + 1
            
#         return ans
            
