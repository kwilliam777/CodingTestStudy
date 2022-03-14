class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [i for i in (path.split("/")) if len(i)>=1 and i != "."]
        path.append(0)
        result = ""
        prev = []
        for i in range(len(path)-1):
            if path[i] != '..':
                result += "/"+path[i]
                prev.append(path[i])
            
            if path [i+1] == '..' and len(prev) >= 1:
                result = result[:-(len(prev[-1])+1)]
                prev.pop()
                
                
        return result if len(result) >= 1 else "/"
    
    
# class Solution(object):
#     def simplifyPath(self, path):
#         stack = []
#         for p in path.split("/"):
#             if p == '..' and len(stack) > 0:
#                 stack.pop()
#             if p == '' or p == '.' or p =='..':
#                 continue
#             else:
#                 stack.append(p)
#         return '/' + '/'.join(stack)
