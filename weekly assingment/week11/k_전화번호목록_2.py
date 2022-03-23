def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        if len(pb[i]) < len(pb[i+1]) and pb[i] == pb[i+1][:len(pb[i])]:
            return False
    return True
