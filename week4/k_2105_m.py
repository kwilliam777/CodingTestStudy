class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        capA = capacityA
        capB = capacityB
        refill = 0
        length = [len(plants)//2,True] if len(plants)%2 == 0 else [len(plants)//2,False]
        for i in range(length[0]):
            if plants[i] <= capA:
                capA -= plants[i]
            else:
                refill += 1
                capA = capacityA
                capA -= plants[i]
            if plants[-i-1] <= capB:
                capB -= plants[-i-1]
            else:
                refill += 1
                capB = capacityB
                capB -= plants[-i-1]

        if length[1] == False:
            temp = max(capA,capB)
            if temp < plants[length[0]]:
                return refill+1
        return refill