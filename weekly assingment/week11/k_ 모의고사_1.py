def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            count1 += 1
        if answers[i] == two[i%8]:
            count2 += 1
        if answers[i] == three[i%10]:
            count3 += 1
            
    high = max(count1,count2,count3)
    ans = []
    if count1 == high:
        ans.append(1)
    if count2 == high:
        ans.append(2)
    if count3 == high:
        ans.append(3)
        
    return ans
