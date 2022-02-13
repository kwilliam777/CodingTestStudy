1390 m x
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            count = 0
            temp = [1,num]
            for i in range(2,num+1//2):
                if count > 2: break
                # print(i,num,temp,count)
                if num%i == 0:
                    count += 1
                    temp.append(num/i)
            if count == 4:
                result += int(sum(temp))
        return result
    
# import math 
# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         result=0
#         for i in nums:
#             right=i+1
#             count=2
#             for j in range(2, int(math.sqrt(i))+1):
#                 if i%j==0:
#                     if (i / j == j) :
#                         count+=1
#                         right+=j
#                     else :
#                         count+=2
#                         right+=j+int(i/j)
#             if count==4:
#                 result+=right
#         return result
