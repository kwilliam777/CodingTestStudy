class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
#         ans = [[1]]
#         for i in range(1,numRows):
#             temp = [1]
#             for j in range(len(ans[-1])-1):
#                 temp.append(ans[-1][j]+ans[-1][j+1])
#             temp.append(1)
#             ans.append(temp)
#             # ans.append(approw(ans[-1],i))
            
            
#         return ans

        
        
        def approw(pre,ind):
            ans = [1]
            for i in range(len(pre)-1):
                ans.append(pre[i]+pre[i+1])
            ans.append(1)
            return ans
        
        ans = [[1]]
        for i in range(1,numRows):
            ans.append(approw(ans[-1],i))
            
            
        return ans
