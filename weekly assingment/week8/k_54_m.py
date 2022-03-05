class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1: return matrix[0]
        
        stop = False
        result = []
        temp = matrix
        while not stop:
            print(temp)
            result += list(temp.pop(0))
            temp = [[temp[j][i] for j in range(len(temp))] for i in range(len(temp[0])-1,-1,-1)]
            if len(temp) == 1:
                result+=temp[0]
                stop = True
        return result
