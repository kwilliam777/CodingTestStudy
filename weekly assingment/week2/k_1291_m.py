class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        first = str(low)[0]
        length = len(str(low))
        num = ""
        result = []
        
        def addNum(first, length, result, num):
            check1 = False
            check2 = False
            temp = first
            if 10-int(temp) < length:
                length += 1
                temp = 1
                check1 = True
            
            for i in range(length):
                num += str(temp)
                temp = int(temp)
                temp += 1

            if int(num) <= high:
                if int(num) >= low:
                    result.append(num)
                
                if int(str(num)[-1]) == 9:
                    # print(str(num)[-1])
                    length += 1
                    temp = 0
                    check2 = True
                    
                num = ""
                if check1:
                    addNum(2, length, result, num)
                elif check2:
                    addNum(temp+1, length, result, num)
                else:
                    addNum(int(first)+1, length, result, num)

        addNum(first, length, result, num)
        
        return result