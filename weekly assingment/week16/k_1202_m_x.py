class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(pairs)==0: return s
        connected = [pairs.pop()]
        ans = list(s)

        while pairs:
            temp = pairs.pop()
            for i in range(len(connected)):
                if temp[0] in connected[i] or temp[1] in connected[i]:
                    connected[i]+=temp
                    break
                if i == len(connected)-1:
                    connected.append(temp)
                    
        connected = [sorted(list(set(i))) for i in connected]

        for i in 
        
        
        for i in connected:
            temp = [ans[j] for j in range(len(ans)) if j in i]
            temp.sort()
            
            
            for j in range(len(i)):
                ans[i[j]] = temp[j]

        return ('').join(ans)
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx    
# class Solution:
#     def smallestStringWithSwaps(self, s, pairs):
#         d = defaultdict(list)
#         for a,b in pairs:
#             d[a].append(b)
#             d[b].append(a)
#         #
#         def dfs(x,A):
#             if x in d:
#                 A.append(x)
#                 for y in d.pop(x):
#                     dfs(y,A)
#         #
#         s    = list(s)
#         while d:
#             x = next(iter(d))
#             A = []
#             dfs(x,A)
#             A = sorted(A)
#             B = sorted([ s[i] for i in A ])
#             for i,b in enumerate(B):
#                 s[A[i]] = b
#         return ''.join(s)
