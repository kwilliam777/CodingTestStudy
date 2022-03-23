def solution(genres, plays):
    tot = {}
    for i in range(len(genres)):
        if genres[i] in tot:
            tot[genres[i]].append((i,plays[i]))
        else:
            tot[genres[i]] = [(i,plays[i])]
    
    order = []
    for i in tot:
        tot[i] = sorted(tot[i], key = lambda x:x[1],reverse = True)
        temp = sum([j[1] for j in tot[i]])
        order.append((i,temp))
    order = sorted(order, key = lambda x:x[1],reverse = True)

    ans = []
    for i in order:
        if len(tot[i[0]]) == 1:
            ans.append(tot[i[0]][0][0])
        else:
            if tot[i[0]][0][1] == tot[i[0]][1][1]:
                ans.append(min(tot[i[0]][0][0],tot[i[0]][1][0]))
                ans.append(max(tot[i[0]][0][0],tot[i[0]][1][0]))
            else:
                ans.append(tot[i[0]][0][0])
                ans.append(tot[i[0]][1][0])    


    return ans
