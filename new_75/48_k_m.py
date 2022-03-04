class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = list(zip(*matrix[::-1]))
        for t in range(len(temp)):
            matrix[t] = list(temp[t])
