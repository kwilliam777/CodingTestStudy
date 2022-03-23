from collections import Counter
def solution(par, com):
    return list(Counter(par) - Counter(com))[0]
