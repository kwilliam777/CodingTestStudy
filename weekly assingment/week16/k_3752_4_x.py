'''
from itertools import combinations
for t in range(int(input())):
    probs = int(input())
    scores = list(map(int, input().split()))
    pos = set()
    for i in range(len(scores)+1):
        pos = set.union(pos,set(map(sum,combinations(scores,i))))
    print("#{} {}".format(t+1,len(pos)))
''' 
for tc in range(1, int(input())+1):
    N = int(input())
    n_li = list(map(int, input().split()))
    a = 1
    for i in n_li:
        a |= a << i
    print('#{} {}'.format(tc, bin(a).count('1')))
