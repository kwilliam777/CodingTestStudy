def solution(numbers, target):
    ans = [0]
    for i in numbers:
        temp = []
        for j in ans:
            temp.append(j+i)
            temp.append(j-i)
        ans = temp
    return ans.count(target)
