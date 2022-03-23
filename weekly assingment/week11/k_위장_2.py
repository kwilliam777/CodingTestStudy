def solution(clothes):
    closet = {}
    for name,typ in clothes:
        if typ in closet:
            closet[typ] += 1
        else:
            closet[typ] = 2
    
    ans = 1
    for i in closet:
        ans *= closet[i]
        
    return ans-1
