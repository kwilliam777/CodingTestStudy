class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(st):
            while "#" in st:
                if len(s)>0 and st[0]=="#":
                    st.pop(0)
                    continue
                ind = st.index("#")
                st.pop(ind)
                st.pop(ind-1)
            return st
        
        return True if check([i for i in s])==check([i for i in t]) else False
    
    
# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#     	s, t = [], []
#     	for i in S: s = s + [i] if i != '#' else s[:-1]
#     	for i in T: t = t + [i] if i != '#' else t[:-1]
#     	return s == t
