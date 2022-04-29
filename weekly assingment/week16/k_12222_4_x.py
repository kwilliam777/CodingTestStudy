for t in range(1, int(input()) + 1):
    st = input()
    div = []
    ind = 0
    while ind < len(st):
        for j in range(ind+1,len(st)+1):
            if  j == len(st):
                if st[ind:j] not in div:
                    div.append(st[ind:j])
                ind = len(st)
                break
            if st[ind:j] not in div:
                div.append(st[ind:j])
                ind = j                
                break
    print("#{} {}".format(t, len(div)))
'''
for tc in range(1, int(input())+1):
    string = input()
    K, i = 1, 0
    last = string[i]
    while i < len(string) - 1:
        if len(last) < 2:
            if last != string[i+1]:
                last = string[i+1]
                i += 1
            else:
                last = string[i+1:i+3]
                i += 2
        else:
            last = string[i+1]
            i += 1
        K += 1 
    print(f'#{tc} {K-(i-len(string)+1)}')
'''
