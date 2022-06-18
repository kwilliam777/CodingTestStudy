class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        target = [tuple(i) for i in target]
        temp = list(zip(*mat[::-1]))
        for _ in range(4):
            if temp == target: return True
            temp = list(zip(*temp[::-1]))

        return False
