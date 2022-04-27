from collections import Counter
for t in range(1,int(input())+1):
    num, turn = list(map(int,input().split()))
    num = list(str(num))
    mx = sorted(num,reverse=True)
    pos = {}
    for i in list(set(num)):
        pos[i] = sorted([j for j in range(len(num)) if num[j] == i])
    
    temp = num
    for i in range(len(temp)):
        if turn==0: break
        if temp[i]!=mx[i]:
            #print(1,temp)
            ind = pos[mx[i].pop()]
            pos[mx[i].insert(0,)
            temp[],temp[i] = temp[i],temp[temp.index(mx[i])]
            #print(2,temp)
            turn-=1
            
    if turn%2==0: print("#{} {}".format(t,('').join(temp)))
    else:
        (temp[-1],temp[-2])=(temp[-2],temp[-1])
        print("#{} {}".format(t,('').join(temp)))

        
        
        
'''
def cal(chan, cnt, k, nums_c):
 
    if chan == cnt:
        str_num = list( map(str,nums_c) )
        int_num = int("".join(str_num))
        global maxx
        if maxx< int_num:
            maxx = int_num
        # print(int_num)
        return
    else:
        piv = nums_c[k]
        temp = nums_c[k+1:]
        val = max(temp)
        if val > piv:                     ## 바꿀 수 있을 때
            for i in range(len(temp)):
                if temp[i] == val:
                    cop = nums_c[:]
                    cop[k], cop[i+k+1] = cop[i+k+1], cop[k]
                    cal(chan,cnt+1,k+1,cop)
        else:  # 바꿀 수 없을 때,
            if k == len(nums_c)-2:
                if len(set(nums_c)) < len(nums_c):  ## 중복 있을 때 그대로
                    cal(chan, chan, k + 1, nums_c)
                    return
                else:
                    if (chan-cnt)%2 == 0:
                        cal(chan, chan, k + 1, nums_c)
                        return
                    else:
                        nums_c[-1], nums_c[-2] = nums_c[-2], nums_c[-1]
                        cal(chan, chan, k + 1, nums_c)
                        return
            else:
                cal(chan, cnt, k+1, nums_c)
 
 
 
 
T = int(input())
for _ in range(10):
 
    nums, chan = map(int,input().split())
    nums = list(map(int,str(nums)))
    # print(nums)
    cnt = 0
    maxx = -1
    cal(chan, cnt, 0, nums)
    print("#{} {}".format(_+1, maxx))
'''
