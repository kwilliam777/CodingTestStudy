class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []

        for data in nums :
            answer.append(data*data)

        answer.sort()
        
        return answer

