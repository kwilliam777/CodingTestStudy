from collections import defaultdict
def solution(survey, choices):
    def check(one,two,mbti):
        if mbti[one]<mbti[two]: 
            return two
        elif mbti[one]>mbti[two]: 
            return one
        else: 
            return min(one,two)
        
    mbti = defaultdict(int)
    for i in range(len(survey)):
        left,right = [*survey[i]]
        choice = choices[i]
        if choice>4: 
            mbti[right]+=choice-4
        elif choice<4: 
            mbti[left]+=4-choice
        
    return check("R","T",mbti)+check("C","F",mbti)+check("J","M",mbti)+check("A","N",mbti)
