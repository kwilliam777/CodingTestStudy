def solution(d):
    sin = False
    dou = False
    tri = False
    star = False
    twostar = False
    starc = 0
    acha = False
    check = False
    score = 0
    for i in range(len(d)-1,-1,-1):
        if check:
            check = not check
        elif d[i].isdigit():
            if i > 0 and d[i-1].isdigit():
                temp = int(d[i-1:i+1])
                check = True
            else:
                temp = int(d[i])
            if dou: temp = temp**2
            elif tri: temp = temp**3
            if starc>0: 
                temp += temp
                if twostar: 
                    temp+=temp
                    twostar=False
                starc-=1
            if acha: temp = -temp
            print(temp)
            score += temp
            sin = False
            dou = False
            tri = False
            star = True if starc > 0 else False
            acha = False
        elif d[i] == "S":
            sin = True
        elif d[i] == "D":
            dou = True
        elif d[i] == "T":
            tri = True
        elif d[i] == "*":
            star = True
            if starc>0:
                twostar=True
            starc = 2
        elif d[i] == "#":
            acha = True
            
    return score





# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)
