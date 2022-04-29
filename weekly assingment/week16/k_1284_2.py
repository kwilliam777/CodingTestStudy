for t in range(1, int(input()) + 1):
    P, Q, R, S, W = list(map(int,input().split()))
    print("#{} {}".format(t,min(P*W,Q if W<=R else Q+(W-R)*S)))
