class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ind = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                [ind.append(j) for j in range(len(matrix[i])) if matrix[i][j] == 0]
                matrix[i] = [0]*len(matrix[i])
                
        for i in range(len(matrix)):
            for j in ind:
                matrix[i][j] = 0
