def solution(numbers):
    numbers = sorted([str(i) for i in numbers],reverse = True)
    for i in range(len(numbers)-1):
        ind = i
        while ind >= 0 and numbers[ind]+numbers[ind+1] < numbers[ind+1]+numbers[ind]:
            temp = numbers[ind]
            numbers[ind] = numbers[ind+1]
            numbers[ind+1] = temp
            ind -= 1
    
    return str(int(("").join(numbers)))


# 개쩐다...
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
