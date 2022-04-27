st = ""
for t in range(1,int(input())+1):
    cnt = str(t).count("3")+str(t).count("6")+str(t).count("9")
    st+= str(t) if cnt==0 else "-"*cnt
    st+=" "
print(st[:-1])
