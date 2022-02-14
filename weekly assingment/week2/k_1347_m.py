class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = {}
        count = 0
        def makedic(dic, l, ind):
            for letter in l:
                if letter in dic:
                    dic[letter][ind] += 1
                else:
                    dic[letter] = [0,0]
                    dic[letter][ind] = 1
        makedic(dic,s,0)
        makedic(dic,t,1)

        for letter in dic:
            count += abs(dic[letter][0] - dic[letter][1])
        
        return int(count/2)
    
        #     훨씬 더 깔끔한 정답 하지만 속도나 효율은 비슷
        # return len(s) - sum((Counter(s) & Counter(t)).values())
                