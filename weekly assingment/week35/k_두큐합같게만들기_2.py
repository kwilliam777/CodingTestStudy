from collections import deque
def solution(queue1, queue2):
    half = sum(queue1+queue2)//2
    val = sum(queue1)
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    length = len(queue1)*2+2
    count = 0
    
    while val!=half:
        if count>length:return -1
        if val < half:
            temp = dq2.popleft()
            val += temp
            dq1.append(temp)
        elif val > half:
            temp = dq1.popleft()
            val -= temp
            dq2.append(temp)
        count+=1
    return count
