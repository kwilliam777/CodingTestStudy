class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openp = remove = []
        
        for i,l in enumerate(s):
            if l == "(": openp.append(i)
            elif l == ")":
                if len(openp) == 0: remove.append(i)
                else: openp.pop()
                    
        s=list(s)
        for i in sorted(openp+remove)[::-1]:
            s.pop(i)
            
        return ("").join(s)
            
