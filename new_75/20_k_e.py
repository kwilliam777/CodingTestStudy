class Solution:
    def isValid(self, s: str) -> bool:
        b,c,r = 0,0,0
        bstack,cstack,rstack = [],[],[]
        
        for l in s:
            if '(' == l:
                b+=1
                bstack.append((c,r))
            elif '{' == l:
                c+=1
                cstack.append((b,r))
            elif '[' == l:
                r+=1
                rstack.append((b,c))
            elif ')' == l:
                b-=1
                if len(bstack) == 0: return False
                temp = bstack.pop()
                if temp != (c,r): return False
            elif '}' == l:
                c-=1
                if len(cstack) == 0: return False
                temp = cstack.pop()
                if temp != (b,r): return False
            elif ']' == l:
                r-=1
                if len(rstack) == 0: return False
                temp = rstack.pop()
                if temp != (b,c): return False

        if b!=0 or c!=0 or r!=0: return False
        
        return True

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         dictt={"(":")","{":"}","[":"]"}
#         for i in s:
#             if i in dictt:
#                 stack.append(i)
#             elif stack==[] or dictt[stack.pop()]!=i:
#                 return False
#         return stack==[]
