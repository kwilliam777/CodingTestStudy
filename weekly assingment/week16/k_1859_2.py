T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    pred = list(map(int,input().split()))
    high = 0
    ans = 0
    for i in range(len(pred)-1,-1,-1):
        if pred[i] > high:
            high = pred[i]
        else:
            ans += high-pred[i]
    print("#{} {}".format(test_case,ans))
