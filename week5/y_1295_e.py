class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0

        for data in nums :
            counter=1
            while data >= 10 :
                counter+=1
                data=int(data/10)
            if counter %2 == 0 :
                answer+=1
                
        return answer
        
