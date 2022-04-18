class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if (start < 0 or start >= len(arr)) or arr[start] < 0: return False
        if arr[start] == 0: return True
        arr[start]=-arr[start]
        ans1 = self.canReach(arr,start-arr[start])
        ans2 = self.canReach(arr,start+arr[start])
        arr[start]=-arr[start]
        return ans1 or ans2
        
        
        
#         visited = [start]
#         stack = [start]
#         count = 0
#         while stack:
#             count+=1
#             if count>40000:break
#             temp = stack.pop()
#             if arr[temp] == 0: return True
#             if temp-arr[temp]>=0 and temp-arr[temp] not in visited:
#                 stack.append(temp-arr[temp])
#                 visited.append(temp-arr[temp])
#             if temp+arr[temp]<len(arr) and temp+arr[temp] not in visited:
#                 stack.append(temp+arr[temp])
#                 visited.append(temp+arr[temp])
            
#         print(visited,stack)
#         return False
            
