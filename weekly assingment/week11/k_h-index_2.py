def solution(citations):
    if citations.count(0) == len(citations): return 0
    high = max(citations)
    
    for i in range(high,0,-1):
        top = [j for j in citations if j >= i]
        bottom = [j for j in citations if j < i]
        if len(top) >= i and len(bottom) <= i:
            return i
        

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
