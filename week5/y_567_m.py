
def array_match (a1,a2) -> bool :
        for i in range(0,len(a1)) :
            if a1[i] != a2[i] :
                return False
        return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (len(s1)>len(s2)):
            return False
        
        s1_a=[]
        s2_a=[]
        
        for i in s1 :
            s1_a.append(i)
        s1_a.sort()
            
        for i in range(0,len(s1)):
            s2_a.append(s2[i])
        s2_a.sort()
        
        num_=len(s1)
        
        #print("**",s1_a)
        
        if array_match(s1_a, s2_a) :
            return True
        
        for i in range(0,len(s2)-len(s1)) :
            s2_a.remove(s2[i])
            s2_a.append(s2[num_+i])
            s2_a.sort()
            if array_match(s1_a, s2_a) :
                return True
        
        return False
        
   
        
