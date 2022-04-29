# 7/20 correct
'''
for t in range(int(input())):
    H,W,N = list(map(int,input().split()))
    st = list(map(len,input().split()))
              
    sign = [W]*H
    long = W//max(st)
    ans = long
    found = False
    for i in range(long,0,-1):
        if found: break
        scale = [j*i for j in st]
        row = i
        temp = W
        for j in range(len(scale)):
            temp -= scale[j]
            if temp < 0:
                if row >= (H//i)*i:
                    break
                else:
                    row+=i
                    if row>(H//i)*i:break
                    temp = W-scale[j]
            elif temp < i*2:
                if j == len(scale)-1:
                    print("#{} {}".format(t+1,i))
                    found=True
                    break
                else:
                    row+=i
                    if row>(H//i)*i:break
                    temp = W
            else:
                if j == len(scale)-1:
                    print("#{} {}".format(t+1,i))
                    found = True
                    break
                else:
                    temp-=i          
'''                    
                    
                    
                    
T = int(input())
for t in range(1, T + 1):
    h, w, n = map(int, input().split())
    words = [len(i) for i in input().split()]
    size = int((h*w/sum(words))**(1/2))
    if size == 1:
        print('#'+str(t), size)
    else:
        for i in range(size, 0, -1):
            if max(words)*i > w or i > h:
                continue
            x, y = 0, 0
            for word in words:
                if x + (1 + word)*i > w or x == 0:
                    x = word*i
                    y += i
                else:
                    x += (1 + word)*i
            if y > h:
                continue
            else:
                print('#' + str(t), i)
                break
