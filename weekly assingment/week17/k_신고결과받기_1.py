from collections import defaultdict
def solution(id_list, report, k):
    rec = defaultdict(list)
    answer = [0 for i in id_list]
    
    for i in list(set(report)):
        key,val = i.split(" ")
        rec[val].append(key)
    
    for i in rec:
        if len(rec[i])>=int(k):
            for j in rec[i]:
                answer[id_list.index(j)]+=1
    
    return answer
